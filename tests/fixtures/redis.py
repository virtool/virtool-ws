import aioredis
import pytest


@pytest.fixture
async def redis(redis_connection_string: str) -> aioredis.Redis:
    """
    A Redis object with pubsub already initialized.

    This ensures that there is no significant delay in creating
    a pubsub subscription. Such a delay could cause messages to be missed.


    :return: A redis connection
    """
    redis = await aioredis.create_redis_pool(redis_connection_string)

    try:
        await redis.ping()
        yield redis
    finally:
        redis.close()
        await redis.wait_closed()
