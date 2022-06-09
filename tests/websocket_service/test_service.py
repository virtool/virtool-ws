import asyncio
import json

from virtool_ws.websocket.listener import dispatcher_messages


async def test_redis_does_receive_messages_from_dispatch_channel(redis):
    channel_name = "channel:dispatch"

    async def read_messages():
        messages = []
        async for message in dispatcher_messages(channel_name, redis):
            messages.append(message)
            if len(messages) >= 10:
                break

        return messages

    task = asyncio.create_task(read_messages())

    await asyncio.sleep(0.25)

    for i in range(10):
        await redis.publish(channel_name, json.dumps({"message": i}))

    _messages = await task

    assert _messages == [{"message": i} for i in range(10)]
