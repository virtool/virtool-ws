from logging import getLogger
from typing import List
from asyncio import CancelledError
from aioredis import Redis

from virtool_ws.websocket.change import Change
from virtool_ws.websocket.connection import Connection
from virtool_ws.websocket.listener import dispatcher_messages
from virtool_ws.websocket.operations import DELETE, INSERT, UPDATE

logger = getLogger(__name__)


class Dispatcher:
    def __init__(self, channel_name: str, redis: Redis):
        self._channel_name = channel_name
        self._redis = redis
        self._connections = list()

    async def run(self):
        """
        Start the dispatcher.

        The dispatcher loops through available changes in the ``listener`` and dispatches them as
        messages to connected websocket clients.

        """
        logger.info("Started dispatcher")

        try:
            async for message in dispatcher_messages(self._channel_name, self._redis):
                change = Change(message["interface"], message["operation"], message["resource"])
                await self._dispatch(change)
                logger.info(f"Received change: {change.target}")
        except CancelledError:
            pass

        logger.debug("Stopped listening for changes")

        await self.close()

    def add_connection(self, connection: Connection):
        """
        Add a connection to the dispatcher.

        :param connection: the connection to add

        """
        self._connections.append(connection)
        logger.debug(f"Added connection to dispatcher: {connection.user_id}")

    def remove_connection(self, connection: Connection):
        """
        Remove a connection from the dispatcher. Make sure it is closed first.

        :param connection: the connection to remove

        """
        try:
            self._connections.remove(connection)
            logger.debug(f"Removed connection from dispatcher: {connection.user_id}")
        except ValueError:
            pass

    @property
    def authenticated_connections(self) -> List[Connection]:
        """
        A list of the authenticated connections tracked by the dispatcher.

        """
        return [conn for conn in self._connections if conn.user_id]

    async def _dispatch(self, change: Change):
        """
        Dispatch a ``message`` with a conserved format to authenticated connections.

        :param change: the change to dispatch

        """
        if change.operation not in (DELETE, INSERT, UPDATE):
            raise ValueError(f"Unknown dispatch operation: {change.operation}")

        for connection in self._connections:
            try:
                await connection.send({
                    "interface": change.interface,
                    "operation": change.operation,
                    "resource": change.resource
                })
            except RuntimeError as err:
                if "RuntimeError: unable to perform operation on <TCPTransport" in str(
                    err
                ):
                    self.remove_connection(connection)

        logger.debug(f"Dispatcher sent messages for {change.target}")

    async def close(self):
        """
        Stop the dispatcher and close all connections.

        """
        logger.debug("Closing dispatcher")

        for connection in self._connections:
            await connection.close()

        logger.debug("Closed dispatcher")
