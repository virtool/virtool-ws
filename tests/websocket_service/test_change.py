from virtool_ws.websocket.change import Change
from virtool_ws.websocket.operations import UPDATE


def test_change():
    """
    Make sure a change object has the required attributes and string representation.

    """
    change = Change("jobs", UPDATE, {"sample": "nuv", "virus": 19})

    assert change.interface == "jobs"
    assert change.operation == UPDATE
    assert change.resource == {"sample": "nuv", "virus": 19}

    assert change.target == "jobs.update"
