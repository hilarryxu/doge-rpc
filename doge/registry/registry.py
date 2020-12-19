# -*- coding: utf-8 -*-

from typing import Callable, Dict

from doge.common.doge import Registry
from doge.common.url import URL


class DirectRegistry(Registry):
    """Fake Registry"""

    def __init__(self, url: URL) -> None:
        self.url = url

    def register(self, service, url):
        pass

    def deregister(self, service, url):
        pass

    def discovery(self, service: str) -> Dict[str, str]:
        address = self.url.get_param("address")
        if address:
            return {str(i): add for i, add in enumerate(address.split(","))}
        return {"0": "%s:%s" % (self.url.host, str(self.url.port))}

    def watch(self, service: str, callback: Callable) -> None:
        pass

    def destroy(self) -> None:
        pass
