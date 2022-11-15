import sys

sys.path.append('C:\\Users\\csayart\\PycharmProjects\\pythonProject11\\Python_Testing_ProjetOC11\\tests')
import fixtures

mock_load = fixtures.mock_loadCompetitions_and_loadClubs


def test_purchase_available_places(client, mock_load):
    response = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Fall Classic',
                                                    'places': '12'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Great-booking complete!' in response_data


def test_purchase_more_than_available_places(client, mock_load):
    response = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Fall Classic',
                                                    'places': '14'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Error-there are not enough available places' in response_data