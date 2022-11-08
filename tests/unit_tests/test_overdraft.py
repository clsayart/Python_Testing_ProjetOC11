import sys

sys.path.append('C:\\Users\\csayart\\PycharmProjects\\pythonProject11\\Python_Testing_ProjetOC11\\tests')
import fixtures

mock_load = fixtures.mock_loadCompetitions_and_loadClubs


def test_purchase_less_than_points(client, mock_load):
    response = client.post('/purchasePlaces', data={'club': 'Iron Temple', 'competition': 'Fall Classic',
                                                    'places': '3'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Great-booking complete!' in response_data


def test_purchase_equal_points(client, mock_load):
    response = client.post('/purchasePlaces', data={'club': 'Iron Temple', 'competition': 'Fall Classic',
                                                    'places': '4'})
    response_data = response.data.decode()
    assert response.status_code == 200
    assert 'Great-booking complete!' in response_data


def test_purchase_more_than_points(client, mock_load):
    response = client.post('/purchasePlaces', data={'club': 'Iron Temple', 'competition': 'Fall Classic',
                                                    'places': '5'})
    response_data = response.data.decode()
    # print("more", response_data)
    assert response.status_code == 200
    assert 'Error-you do not have enough points' in response_data
