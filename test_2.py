from api.BoardApi import BoardApi
import pytest
# Предположим, что у вас есть переменные с вашими ключом и токеном
API_KEY = "<your_api_key>"
API_TOKEN = "<your_api_token>"
BASE_URL = "https://api.trello.com/1"

@pytest.fixture
def board_api():
    return BoardApi(BASE_URL, API_KEY, API_TOKEN)

def test_get_boards(board_api):
    boards = board_api.get_boards()
    assert isinstance(boards, list), "Метод get_boards должен возвращать список"

def test_create_board(board_api):
    new_board_name = "Test Board"
    created_board = board_api.create_board(new_board_name)
    assert created_board["name"] == new_board_name, f"Доска должна называться {new_board_name}"

def test_delete_board(board_api):
    # Создаем временную доску для удаления
    temp_board_id = board_api.create_board("Temp Test Board")["id"]
    result = board_api.delete_board(temp_board_id)
    assert result is True, "Доска должна быть успешно удалена"