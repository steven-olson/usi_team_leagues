from django.contrib import admin

from teams_leagues_viewer.models import Team, League


class TeamTabularInline(admin.TabularInline):
    model = Team


class LeagueAdmin(admin.ModelAdmin):
    inlines = [TeamTabularInline]
    model = League
    list_display = ['abbr', 'name']


admin.site.register(League, LeagueAdmin)
