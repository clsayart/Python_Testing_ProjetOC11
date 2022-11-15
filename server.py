import json
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions)
    except IndexError:
        return render_template('index.html', message="Unknown email, please enter only a registered email")


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club][0]
    foundCompetition = [c for c in competitions if c['name'] == competition][0]
    if foundClub and foundCompetition:
        return render_template('booking.html', club=foundClub, competition=foundCompetition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


# @app.route('/purchasePlaces', methods=['POST'])
# def purchasePlaces():
#     competition = [c for c in competitions if c['name'] == request.form['competition']][0]
#     club = [c for c in clubs if c['name'] == request.form['club']][0]
#     # print("club, competition", club, competition)
#     try:
#         club[f"{competition['name']}_counter"]
#     except KeyError:
#         club[f"{competition['name']}_counter"] = 0
#     # print("club, competition", club, competition)
#     placesRequired = int(request.form['places'])
#     if placesRequired > int(competition['numberOfPlaces']):
#         flash('Error-there are not enough available places to complete this purchase')
#         if placesRequired + club[f"{competition['name']}_counter"] < 13:
#             if placesRequired > int(club['points']):
#                 flash('Error-you do not have enough points available to complete the purchase')
#             else:
#                 competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
#                 club[f"{competition['name']}_counter"] += placesRequired
#                 club['points'] = int(club['points']) - placesRequired
#                 flash('Great-booking complete!')
#         else:
#             flash('Error-you cannot purchase more than 12 places')
#     return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    # print("club, competition", club, competition)
    try:
        club[f"{competition['name']}_counter"]
    except KeyError:
        club[f"{competition['name']}_counter"] = 0
    # print("club, competition", club, competition)
    placesRequired = int(request.form['places'])
    if placesRequired > int(competition['numberOfPlaces']):
        flash('Error-there are not enough available places to complete this purchase')
    elif placesRequired + club[f"{competition['name']}_counter"] >= 13:
        flash('Error-you cannot purchase more than 12 places')
    elif placesRequired > int(club['points']):
        flash('Error-you do not have enough points available to complete the purchase')
    else:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
        club[f"{competition['name']}_counter"] += placesRequired
        club['points'] = int(club['points']) - placesRequired
        flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display
@app.route('/displayPoints', methods=['GET'])
def display_points():
    return render_template('board.html', clubs=clubs)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
