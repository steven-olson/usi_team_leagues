<h1>Overview</h1>

Quick and simple django app that loads in two csvs and displays them on the index page.


<h2>Functional Requirements</h2>
- Create an app with two models, league and team. The csv files provided (league and team) should be imported into the models. The team model will be a one-to-many of league.

- Provide an admin for league with team as an inline.
- Create a user and allow access to the Django admin. The user should only have access to change leagues but should allow access to add/change/delete teams.
- Offer a page that loads at the root url (http://localhost:8000/) that lists all the leagues and teams under each league.

<h2>Implementation tldr</h2>

The focal point here are the two management commands that load in the csv. Besides that,
its really just a super simple view plus two super simple models.

Two unit tests are included for the two commands, both tests run through the entire
ETL processes quite nicely. I didn't really feel that more tests were warranted given
the scope of this work and the rest of the code (the two commands are the only technically
interesting things here, you can eyeball everything else).



<h2>How to run</h2>
Pretty standard django stuff, the only nuance being that we need to run our setup command

1. Get the code (probably by cloning the repo)
2. cd into main dir
3. create a virtual env, I use venv: ```python -m venv venv```
4. Activate virtual env: ```source ./venv/bin/activate```
5. install packages: ```pip install -r requirements.txt```
6. run migrations: ```python manage.py migrate```
7. run setup command: ```python manage.py setup```
8. run the actual app: ```python manage.py runserver```