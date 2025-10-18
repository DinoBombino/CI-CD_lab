import pytest
import requests
from app import app  # Для локальных тестов

BASE_URL = 'http://localhost:5000'

def setup_module():
    with app.app_context():
        from app import db, Calculation
        db.create_all()  # Инициализация БД для тестов

def test_add():
    response = requests.post(f'{BASE_URL}/calculate', json={'a': 2, 'b': 3, 'op': 'add'})
    assert response.status_code == 200
    assert response.json()['result'] == 5

def test_subtract():
    response = requests.post(f'{BASE_URL}/calculate', json={'a': 8, 'b': 3, 'op': 'subtract'})
    assert response.status_code == 200
    assert response.json()['result'] == 5

def test_invalid_op():
    response = requests.post(f'{BASE_URL}/calculate', json={'a': 2, 'b': 3, 'op': 'invalid'})
    assert response.status_code == 400

def test_history():
    response = requests.get(f'{BASE_URL}/history')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_functions():
    from app import add, min
    assert add(2, 3) == 5
    assert add(3, 3) == 6
    assert add(3, 4) == 7
    assert add(-1, 1) == 0
    assert min(8, 3) == 5