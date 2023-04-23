from django.core.management.base import BaseCommand
from teams_leagues_viewer.models import League
import csv
import logging
import os

from teams_leagues.settings import BASE_DIR

log = logging.getLogger(__name__)

BASE_CSV_PATH = os.path.join(BASE_DIR, "teams_leagues_viewer", "data", "leagues.csv")


class Command(BaseCommand):
    help = "Utility command for loading in a new league csv into our system"

    def add_arguments(self, parser):
        parser.add_argument(
            "--path_to_csv",
            type=str,
            default=""
        )

        parser.add_argument(
            "--commit",
            action="store_true",
            help="Actually commit to db",
            default=False
        )

        parser.add_argument(
            "--purge_existing",
            action="store_true",
            help="Get rid of what we already have",
            default=False
        )

        parser.add_argument(
            "--skip_header",
            action="store_true",
            help="If this csv has a header, skip it",
            default=True
        )

    def handle(self, *args, **options):

        path_to_csv = options.get("path_to_csv") or BASE_CSV_PATH
        should_commit = options.get("commit") or False
        purge_existing = options.get("purge_existing") or False
        skip_header = options.get("skip_header") or True

        if purge_existing:
            League.objects.all().delete()

        created_leagues = []
        row_number = 0

        with open(path_to_csv) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:

                if skip_header is True and row_number == 0:
                    # skip header row
                    row_number = row_number + 1
                    continue

                created_league = self._create_league_from_row(row, row_number)

                if created_league:
                    log.info(f"Created new league {created_league}!")
                    created_leagues.append(created_league)

                row_number = row_number + 1

        if should_commit:
            League.objects.bulk_create(created_leagues)
        else:
            log.info(f"Dry run, would have committed {len(created_leagues)} leagues")

    @staticmethod
    def _create_league_from_row(row, row_number) -> League | None:
        try:
            abbr = row[1]
            name = row[2]

            assert abbr is not None and isinstance(abbr, str)
            assert name is not None and isinstance(name, str)

        except Exception as e:
            log.info(f"Failed handling row {row_number}!\n{e}")
            return None

        return League(
            abbr=abbr,
            name=name
        )
