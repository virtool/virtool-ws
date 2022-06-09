import logging

from aiohttp.web_app import Application
from aiojobs.aiohttp import get_scheduler_from_app
from virtool_core.redis import connect
from virtool_ws.websocket.dispatcher import Dispatcher

logger = logging.getLogger("startup")


async def set_scheduler(app: Application):
    app["scheduler"] = get_scheduler_from_app(app)


async def startup_dispatcher(app: Application):

    logger.info("Starting dispatcher")

    channel = "channel:dispatch"

    app["dispatcher"] = Dispatcher(
        channel, app["redis"]
    )

    await get_scheduler_from_app(app).spawn(app["dispatcher"].run())


async def startup_redis(app: Application):
    """
    Connects to MongoDB, Redis and Postgres concurrently

    :param app: the app object

    """
    redis_connection_string = app["redis_connection_string"]
    timeout = 1

    redis = await connect(redis_connection_string, timeout)

    app["redis"] = redis
