# I absolutely hate django tests its insane this needs to be
# set at import time if you want to step into the test
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teams_leagues.settings')

# I hate django tests, this has to go first
import django
django.setup()

from django.core.management import call_command
from django.test import TestCase
from teams_leagues_viewer.models import Team, League


class CommandsTestCase(TestCase):

    def test_league_command(self):
        # Delete everything at the start. Obviously using the same db for tests and "prod"
        # is silly, but for the sake of this coding challenge, I think its fine
        League.objects.all().delete()
        Team.objects.all().delete()

        # We want to set up our leagues first
        call_command(
            "load_leagues_csv",
            "--commit"
        )

        # then load in our actual teams
        call_command(
            "load_teams_csv",
            "--commit"
        )

        # We assume that we used the default csv file here
        self.assertTrue(Team.objects.all().count() == 124)

        # Make sure first one looks good
        first = Team.objects.first()
        self.assertTrue(first.name == 'Anaheim Ducks')
        self.assertTrue(first.abbr == "ANA")
        self.assertTrue(first.league_id == 3)
