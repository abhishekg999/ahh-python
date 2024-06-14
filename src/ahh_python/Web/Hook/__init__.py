from time import sleep
import json
import base64
import os
from socketio import Client
from typing import Generator
from dataclasses import dataclass


@dataclass
class WebhookRequest:
    body: str
    raw_headers: str
    headers: dict[str, str]
    ip: str
    method: str
    path: str


class RequestBinWebhook:
    def __init__(self, api_key=None):
        self.api_key = api_key if api_key else os.getenv("REQUESTBIN_APIKEY")
        if not self.api_key:
            raise Exception(
                "Missing RequestBin API Key. Either pass as an argument or set the REQUESTBIN_APIKEY env variable."
            )

        self.sio = Client()
        self.url = f"https://{self.api_key}.x.pipedream.net/"

        self.requests = []

        self._path_ignore = []

        @self.sio.on("request")
        def request(data):
            data = json.loads(data)["step"]["request"]
            data["body"] = base64.b64decode(data["body"]).decode("latin-1")
            self.requests.append(data)

    def __enter__(self):
        self.sio.connect(
            f"https://requestbin-api.pipedream.com/?api_key={self.api_key}",
            socketio_path="/api/v2/public/socket.io",
            transports=["websocket"],
            wait_timeout=20,
        )
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sio.disconnect()
        self.sio.wait()

    def get_requests_sync(self) -> Generator[WebhookRequest, None, None]:
        while True:
            if self.requests:
                request_data = self.requests.pop(0)
                if request_data["path"] in self._path_ignore:
                    continue

                yield WebhookRequest(
                    request_data.get("body", ""),
                    request_data.get("raw_headers", ""),
                    request_data.get("headers", {}),
                    request_data.get("ip", ""),
                    request_data.get("method", ""),
                    request_data.get("path", ""),
                )
            else:
                sleep(0.001)

    def ignore_path(self, path: str):
        self._path_ignore.append(path)


__all__ = ["RequestBinWebhook", "WebhookRequest"]
