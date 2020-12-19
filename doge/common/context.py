# -*- coding: utf-8 -*-

from doge.common.doge import Registry
from doge.common.exceptions import RegistryCfgError
from doge.common.url import URL
from doge.registry.registry import DirectRegistry


class Context:
    def __init__(self, url: URL, registry_url: URL) -> None:
        self.url = url
        self.registry_url = registry_url

    def get_registry(self) -> Registry:
        protocol = self.registry_url.get_param("protocol", "direct")
        if protocol == "direct":
            return DirectRegistry(self.registry_url)
        raise RegistryCfgError
