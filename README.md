It consists of creating a Django app that will house two models and offer a landing page which will output the data along with access to an admin section. The following breaks down the requirements.

- Create an app with two models, league and team. The csv files provided (league and team) should be imported into the models. The team model will be a one-to-many of league.

- Provide an admin for league with team as an inline.
- Create a user and allow access to the Django admin. The user should only have access to change leagues but should allow access to add/change/delete teams.
- Offer a page that loads at the root url (http://localhost:8000/) that lists all the leagues and teams under each league.