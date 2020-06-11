from fastapi.testclient import TestClient

from server.app import app


client = TestClient(app)


def test_plugins():
    """Test general /plugins endpoint"""
    good_response = client.post(
        "/plugins",
        headers={},
        json={
            "query_str": "test",
            "other_content": "some other content"
        },
    )

    bad_response = client.post(
        "/plugins",
        headers={},
        json={
            # no content (required)
            "other_content": "some other content"
        },
    )

    assert good_response.json() == {
        "answer_str": "@Parameters(name=\"namestring\")\n",
        "plugin": None,
        "other_content": None,
    }
    assert good_response.status_code == 200

    assert bad_response.status_code == 422 # unprocessable


def test_plugin():
    """Test specific /plugins/{plugin} endpoint"""
    good_response = client.post(
        "/plugins/testplugin",
        headers={},
        json={
            "query_str": "test",
            "other_content": "some other content"
        },
    )

    bad_response = client.post(
        "/plugins/testplugin",
        headers={},
        json={
            # no content (required)
            "other_content": "some other content"
        },
    )

    assert good_response.json() == {
        "answer_str": "@Parameters(name=\"namestring\")\n",
        "plugin": "testplugin",
        "other_content": None,
    }
    assert good_response.status_code == 200

    assert bad_response.status_code == 422 # unprocessable


def test_root():
    """Test root / endpoint"""
    response = client.get('/')
    assert response.status_code == 404
