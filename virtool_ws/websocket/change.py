from dataclasses import dataclass
from typing import Any, Dict

from virtool_ws.websocket.operations import Operation


@dataclass
class Change:
    """
    Represents a change in a resource.

    For now, only used to trigger the dispatch of websocket messages containing a minimal update of
    the resource to connected browser clients.

    """

    interface: str
    operation: Operation
    resource: Dict[str, Any]

    @property
    def target(self):
        return f"{self.interface}.{self.operation}"