#coding=utf-8
from handlers import *

wwwUrls = [
    (r'/api/get_token', ApiUpTokenHdl),
    (r'/api/q_callback', ApiUpCallbackHdl),
    (r'/api/q_notify', ApiPersistentNotifyHdl),
]