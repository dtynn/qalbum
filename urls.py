#coding=utf-8
from handlers import *

wwwUrls = [
    (r'/', PageIndexHdl),
    (r'/api/q_token', ApiUpTokenHdl),
    (r'/api/q_callback', ApiUpCallbackHdl),
    (r'/api/q_notify', ApiPersistentNotifyHdl),
]