import sys

sys.path.append('C:\\Users\\csayart\\PycharmProjects\\pythonProject11\\Python_Testing_ProjetOC11\\tests')
import fixtures

mock_load = fixtures.mock_loadCompetitions_and_loadClubs


def test_display_board(client, mock_load):
    response = client.get('/displayPoints')
    response_data = response.data.decode()
    print(response_data)
    assert response.status_code == 200
    assert 'GUDLFT CLUBS' and 'CLUBS' in response_data


