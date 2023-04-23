#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teams_leagues.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    print(sys.argv)
    execute_from_command_line(sys.argv)


def debug_main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teams_leagues.settings')
    from django.core.management import execute_from_command_line
    from django.core.management import call_command

    execute_from_command_line(["manage.py", "runserver"])


if __name__ == '__main__':

    debug_main()

    #main()
