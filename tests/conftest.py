import pytest


pytest_plugins = [
    "tests.fixtures.app",
    "tests.fixtures.websocket",
    "tests.fixtures.redis"
]


@pytest.fixture
def redis_connection_string(request):
    return request.config.getoption("--redis-connection-string")


def pytest_addoption(parser):
    parser.addoption(
        "--redis-connection-string",
        action="store",
        default="redis://localhost:6379",
    )
