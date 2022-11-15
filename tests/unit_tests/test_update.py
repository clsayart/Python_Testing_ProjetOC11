import sys

sys.path.append('C:\\Users\\csayart\\PycharmProjects\\pythonProject11\\Python_Testing_ProjetOC11\\tests')
import fixtures

mock_load = fixtures.mock_loadCompetitions_and_loadClubs


def test_update_points(client, mock_load):
    response = client.post('/purchasePlaces', data={'club': 'Simply Lift', 'competition': 'Spring Festival',
                                                    'places': '3'})
    response_data = response.data.decode()
    print(response_data)
    assert response.status_code == 200
    assert 'Points available: 10' in response_data
    assert 'Great-booking complete!' in response_data