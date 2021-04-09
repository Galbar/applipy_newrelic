from logging import Handler

from newrelic_telemetry_sdk import (
    Log,
    LogClient,
)


class NewRelicLogHandler(Handler):

    _client: LogClient

    def __init__(self, client: LogClient) -> None:
        super().__init__()
        self._client = client

    def emit(self, record):
        self._client.send(Log.from_record(record)).raise_for_status()
