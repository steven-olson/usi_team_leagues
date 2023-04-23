from django.http import HttpResponse
from teams_leagues_viewer.models import League
from django.shortcuts import render


def index(request) -> HttpResponse:
    """
    When someone hits our index page, we want to display all of our
    current leagues, as well as all teams in those leagues.

    For the time being here we just want to pass in all the league
    models, the template will do the iteration

    :param request:
    :return:
    """
    context = {
        "all_leagues": League.objects.all()
    }
    return render(request, "index.html", context)

