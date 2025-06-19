import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import app, Base, get_db

SQLALCHEMY_DATABASE_URL = 'sqlite:///:memory:'

from sqlalchemy.pool import StaticPool

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# override get_db dependency

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_register_and_login():
    Base.metadata.create_all(bind=engine)

    response = client.post('/users/', json={'username': 'alice', 'password': 'secret'})
    assert response.status_code == 200
    data = response.json()
    assert data['username'] == 'alice'

    response = client.post('/token', data={'username': 'alice', 'password': 'secret'})
    assert response.status_code == 200
    token = response.json()['access_token']
    assert token

    response = client.get('/me', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert response.json()['username'] == 'alice'
