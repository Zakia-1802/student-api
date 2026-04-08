import os
import sys

# Ajouter le dossier racine du projet au chemin Python
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app, students


def test_post_student():
    app.config["TESTING"] = True
    client = app.test_client()

    initial_count = len(students)

    new_student = {
        "name": "Zakia",
        "field": "DevOps"
    }

    response = client.post("/students", json=new_student)

    assert response.status_code == 201
    assert response.get_json()["name"] == "Zakia"
    assert response.get_json()["field"] == "DevOps"
    assert len(students) == initial_count + 1


def test_get_info_with_env_variable():
    os.environ["ACADEMY_NAME"] = "Test Academy"

    app.config["TESTING"] = True
    client = app.test_client()

    response = client.get("/info")
    data = response.get_json()

    assert response.status_code == 200
    assert data["academy_name"] == "Test Academy"
    assert "total_students" in data
