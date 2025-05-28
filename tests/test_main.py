from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_get_average():
    response = client.get("/results/average")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "average_token_count" in data
    assert "average_time_to_first_token" in data
    assert "average_time_per_output_token" in data
    assert "average_total_generation_time" in data

    for value in data.values():
        assert isinstance(value, float)


def test_get_average_in_window():
    start_time = "2024-06-01T00:00:00"
    end_time = "2024-06-02T00:00:00"
    response = client.get(f"/results/average/{start_time}/{end_time}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "average_token_count" in data
    assert "average_time_to_first_token" in data
    assert "average_time_per_output_token" in data
    assert "average_total_generation_time" in data

    for value in data.values():
        assert isinstance(value, float)


def test_invalid_time_range():
    start_time = "2024-06-02T00:00:00"
    end_time = "2024-06-01T00:00:00"

    response = client.get(f"/results/average/{start_time}/{end_time}")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["detail"] == "start_time must be before or equal to end_time"
