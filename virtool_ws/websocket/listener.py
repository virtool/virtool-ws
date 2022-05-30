import logging
from aioredis import Redis


async def dispatcher_messages(channel_name: str, redis: Redis):
    """
    Read messages from a redis pub/sub channel.

    :param channel_name: The name of the channel
    :param redis: The redis connection
    :return: Async generator of messages on the channel
    """

    (channel,) = await redis.subscribe(channel_name)

    while True:
        yield await channel.get_json()




