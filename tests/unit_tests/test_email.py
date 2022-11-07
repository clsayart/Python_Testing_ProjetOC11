import sys

sys.path.append('C:\\Users\\csayart\\PycharmProjects\\pythonProject11\\Python_Testing_ProjetOC11\\tests')
import fixtures

mock_load = fixtures.mock_loadCompetitions_and_loadClubs


def test_known_email(client, mock_load):
    response = client.post('/showSummary', data={'email': 'kate@shelifts.co.uk'})
    response_data = response.data.decode()
    # print("response_data known email", response_data)
    assert response.status_code == 200
    assert 'Logout' in response_data


def test_unknown_email(client, mock_load):
    response = client.post('/showSummary', data={'email': 'clairetest@email.com'})
    response_data = response.data.decode()
    # print("response_data unknown email", response_data)
    assert response.status_code == 200
    assert 'Unknown email' in response_data
