# -*- coding: utf-8 -*-

from mprpc import RPCClient

client = RPCClient('127.0.0.1', 4399)
print(client.call('sum', 1, 2))
