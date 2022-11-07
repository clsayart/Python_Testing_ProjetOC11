import sys
import pytest

sys.path.append('C:\\Users\\csayart\\PycharmProjects\\pythonProject11\\Python_Testing_ProjetOC11')
import server


@pytest.fixture
def client():
    server.app.config['TESTING'] = True
    client = server.app.test_client()
    return client
