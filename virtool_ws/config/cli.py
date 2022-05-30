import asyncio

import click
from virtool_ws.app import create_app
from aiohttp import web


def entry():
    start_web_server()


@click.command()
@click.option(
    "--redis-connection-string",
    help="The Redis connection string",
    type=str,
    required=True,
    default="redis://localhost:6379",
)
def start_web_server(redis_connection_string):
    app = create_app(redis_connection_string)
    web.run_app(app)






