from virtool_ws.websocket.dispatcher import Dispatcher


def test_add_and_remove_connection(mocker, redis):
    channel = "channel:dispatch"

    dispatcher = Dispatcher(channel, redis)

    m = mocker.Mock()

    dispatcher.add_connection(m)

    assert m in dispatcher._connections

    dispatcher.remove_connection(m)

    assert dispatcher._connections == []
