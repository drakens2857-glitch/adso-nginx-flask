import pytest
from unittest.mock import patch, MagicMock
from sample_app import sample  

@pytest.fixture
def client():
    sample.config['TESTING'] = True
    with sample.test_client() as client:
        yield client

@patch('sample_app.conectar')
def test_main_route_success(mock_conectar, client):

    mock_db = MagicMock()
    mock_cursor = MagicMock()
    
    mock_conectar.return_value = mock_db
    mock_db.cursor.return_value = mock_cursor

    mock_cursor.fetchall.return_value = []

    response = client.get('/')

    assert response.status_code == 200  # nosec B101
