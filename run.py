from virtool_core.logging import configure_logs

import virtool_ws.config.cli

if __name__ == "__main__":
    configure_logs(debug=True)
    virtool_ws.config.cli.entry()
