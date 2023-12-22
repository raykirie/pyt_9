import pytest
import httpx

API_URL = "http://localhost:3333"


@pytest.fixture
async def client():
    async with httpx.AsyncClient() as client:
        yield client


@pytest.fixture
async def registered_user(client):
    data = {
        "username": "testuser",
        "password": "testpass",
        "email": "testuser@example.com",
        "name": "Test User"
    }

    response = await client.post(API_URL + "/register", json=data)
    assert response.status_code == 201

    return data


@pytest.mark.asyncio
async def test_register(client, registered_user):
    assert "username" in registered_user

    data = {
        "username": registered_user["username"],
        "password": registered_user["password"]
    }

    response = await client.post(API_URL + "/login", json=data)
    assert response.status_code == 200
    assert "access_token" in response.json()


@pytest.mark.asyncio
async def test_get_profile(client, registered_user):
    data = {
        "username": registered_user["username"],
        "password": registered_user["password"]
    }

    response = await client.post(API_URL + "/login", json=data)
    assert response.status_code == 200
    assert "access_token" in response.json()

    token = response.json()["access_token"]

    response = await client.get(API_URL + "/profile", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json() == {
        "username": registered_user["username"],
        "email": registered_user["email"],
        "name": registered_user["name"]
    }


@pytest.mark.asyncio
async def test_update_profile(client, registered_user):
    data = {
        "username": registered_user["username"],
        "password": registered_user["password"]
    }

    response = await client.post(API_URL + "/login", json=data)
    assert response.status_code == 200
    assert "access_token" in response.json()

    token = response.json()["access_token"]

    updated_data = {
        "email": "updated@example.com",
        "name": "Updated User"
    }

    response = await client.put(API_URL + "/profile", headers={"Authorization": f"Bearer {token}"}, json=updated_data)
    assert response.status_code == 200
    assert response.json() == {
        "username": registered_user["username"],
        "email": updated_data["email"],
        "name": updated_data["name"]
    }
