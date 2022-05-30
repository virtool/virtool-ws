import pytest

from virtool_ws.app import create_app


@pytest.fixture
def redis_connection_string():
    return "redis://localhost:6379"


@pytest.fixture
async def app(aiohttp_client, redis_connection_string):
    app = create_app(redis_connection_string)
    _ = await aiohttp_client(app)
    return app
