from fastapi.testclient import TestClient

from server import app


client = TestClient(app)


TEST_QUERIES = [
    {
        "query_str":"test",
        "other_content":"some other content",
        "expected": {
            "code": 200,
        }
    },
    {
        "query_str": None,
        "other_content":"some other content",
        "expected": {
            "code": 422,
        }
    },
]


def test_plugins():
    """Test general /plugins endpoint"""

    for test in TEST_QUERIES:
        response = client.post(
            "/plugins",
            headers={},
            json={
                "query_str": test["query_str"],
                "other_content": test["other_content"]
            },
        )
        assert response.status_code == test["expected"]["code"]


def test_plugin():
    """Test specific /plugins/{plugin} endpoint"""

    for test in TEST_QUERIES:
        response = client.post(
            "/plugins/testplugin",
            headers={},
            json={
                "query_str": test["query_str"],
                "other_content": test["other_content"]
            },
        )
        assert response.status_code == test["expected"]["code"]


def test_root():
    """Test root / endpoint"""
    response = client.get('/')
    assert response.status_code == 404
