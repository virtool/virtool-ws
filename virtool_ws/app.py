import logging
from aiohttp import web
from aiojobs.aiohttp import setup

import virtool_ws.ws
from virtool_ws.startup import set_scheduler, startup_redis, startup_dispatcher

logger = logging.getLogger(__name__)

routes = web.RouteTableDef()


def create_app(redis_connection_string: str) -> web.Application:
    app = web.Application()

    app["redis_connection_string"] = redis_connection_string

    setup(app)

    app.on_startup.extend([set_scheduler, startup_redis, startup_dispatcher])
    app.add_routes(routes)
    app.add_routes([web.get('/ws', virtool_ws.ws.root)])

    return app


