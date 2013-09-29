#coding=utf-8
from base import WwwBaseHdl


class PageIndexHdl(WwwBaseHdl):
    def get(self):
        self.render('upload.html')
        return