import os
import sys

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from main import Base, app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_create_join_and_list_events():
    Base.metadata.create_all(bind=engine)

    # register two users
    client.post("/users/", json={"username": "alice", "password": "secret"})
    res = client.post("/token", data={"username": "alice", "password": "secret"})
    token_alice = res.json()["access_token"]

    client.post("/users/", json={"username": "bob", "password": "secret"})
    res = client.post("/token", data={"username": "bob", "password": "secret"})
    token_bob = res.json()["access_token"]

    # alice creates event
    response = client.post(
        "/events/",
        json={"name": "trip"},
        headers={"Authorization": f"Bearer {token_alice}"},
    )
    assert response.status_code == 200
    event = response.json()
    invitation_token = event["invitation_token"]

    # bob joins using token
    join_res = client.post(
        f"/events/join/{invitation_token}",
        headers={"Authorization": f"Bearer {token_bob}"},
    )
    assert join_res.status_code == 200

    # bob lists events
    list_res = client.get(
        "/events/", headers={"Authorization": f"Bearer {token_bob}"}
    )
    assert list_res.status_code == 200
    events = list_res.json()
    assert len(events) == 1
    assert events[0]["name"] == "trip"
