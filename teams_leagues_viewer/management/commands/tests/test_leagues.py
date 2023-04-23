# I absolutely hate django tests its insane this needs to be
# set at import time if you want to step into the test
import django
django.setup()

from django.core.management import call_command
from django.test import TestCase
import os
from teams_leagues_viewer.models import League, Team


# I absolutely hate django tests its insane this needs to be
# set at import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teams_leagues.settings')


class CommandsTestCase(TestCase):

    def test_league_command(self):
        # Delete everything at the start. Obviously using the same db for tests and "prod"
        # is silly, but for the sake of this coding challenge, I think its fine
        League.objects.all().delete()
        Team.objects.all().delete()

        call_command(
            "load_leagues_csv",
            "--commit"
        )

        # We assume that we used the default csv file here
        self.assertTrue(League.objects.all().count() == 4)

        # Make sure first one looks good
        first = League.objects.first()
        self.assertTrue(first.name == "National Basketball Association")
        self.assertTrue(first.abbr == "NBA")
