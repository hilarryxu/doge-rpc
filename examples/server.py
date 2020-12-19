# -*- coding: utf-8 -*-

import sys
import os
import os.path
from os.path import dirname
import logging

ROOT = os.path.abspath(dirname(dirname(__file__)))  # noqa
sys.path.append(ROOT)  # noqa

from gevent import monkey  # noqa

from doge.common.utils import init_tracer  # noqa
from doge.rpc.server import new_server  # noqa

monkey.patch_socket()


logging.basicConfig(level=logging.DEBUG)


init_tracer("server")


class Sum:
    def sum(self, x, y):
        return x + y


if __name__ == "__main__":
    server = new_server("examples/server.yaml")
    server.load(Sum)
    server.run()
