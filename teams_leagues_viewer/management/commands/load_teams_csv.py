from django.core.management.base import BaseCommand
from teams_leagues_viewer.models import Team, League
import csv
import logging
import os

from teams_leagues.settings import BASE_DIR

log = logging.getLogger(__name__)

BASE_CSV_PATH = os.path.join(BASE_DIR, "teams_leagues_viewer", "data", "teams.csv")


class Command(BaseCommand):
    help = "Utility command for loading in a new team csv into our system"

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
            Team.objects.all().delete()

        created_teams = []
        row_number = 0

        with open(path_to_csv) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:

                if skip_header is True and row_number == 0:
                    # skip header row
                    row_number = row_number + 1
                    continue

                created_team = self._create_team_from_row(row, row_number)

                if created_team:
                    log.info(f"Created new team {created_team}!")
                    created_teams.append(created_team)

                row_number = row_number + 1

        if should_commit:
            Team.objects.bulk_create(created_teams)
        else:
            log.info(f"Dry run, would have committed {len(created_teams)} teams")

    @staticmethod
    def _create_team_from_row(row, row_number) -> Team | None:
        try:
            abbr = row[0]
            name = row[1]
            league_abbr = row[2]

            assert abbr is not None and isinstance(abbr, str)
            assert name is not None and isinstance(name, str)
            assert league_abbr is not None and isinstance(name, str)

        except Exception as e:
            log.info(f"Failed handling row {row_number}!\n{e}")
            return None

        # We also need to fetch the league that this corresponds to
        leagues = League.objects.filter(abbr=league_abbr)
        if leagues.count() == 0:
            teams_league = None
        else:
            teams_league = leagues.first()

        return Team(
            abbr=abbr,
            name=name,
            league=teams_league
        )
