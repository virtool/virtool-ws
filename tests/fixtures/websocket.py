from typing import Dict, Union, Optional, Sequence

import pytest
from aiohttp.test_utils import make_mocked_coro
from aiohttp.web_ws import WebSocketResponse

from virtool_ws.websocket.connection import Connection


class UserClient:
    def __init__(
        self,
        administrator: bool,
        force_reset: bool,
        groups: Sequence[str],
        permissions: Dict[str, bool],
        user_id: Union[str, None],
        authenticated: bool,
        session_id: Optional[str] = None,
    ):
        self._administrator = administrator
        self._force_reset = force_reset
        self._groups = groups
        self._permissions = permissions
        self._user_id = user_id
        self._authenticated = authenticated
        self._session_id = session_id


@pytest.fixture
def ws(mocker):
    ws = mocker.Mock(spec=WebSocketResponse)

    ws.send_json = make_mocked_coro()
    ws.close = make_mocked_coro()

    client = mocker.Mock(spec=UserClient)

    client.user_id = "test"
    client.groups = ["admin", "test"]
    client.permissions = ["create_sample"]

    return Connection(ws, client)
