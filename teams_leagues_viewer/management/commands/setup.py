from django.core.management.base import BaseCommand
import logging
from django.core.management import call_command
from teams_leagues_viewer.models import Team, League
from django.contrib.auth.models import User


log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "This command sets things up for a first run"

    def handle(self, *args, **options):

        # create leagues
        call_command(
            "load_leagues_csv",
            "--commit"
        )

        # then load in our actual teams
        call_command(
            "load_teams_csv",
            "--commit"
        )

        log.info(f"Created {Team.objects.all().count()} teams and {League.objects.all().count()} leagues!")

        # Create a dummy user to satisfy requirement 3?
        User.objects.create_user(
            username='default_user',
            email=None,
            password='password123',
            # we want to have access to admin
            is_staff=True
        )
