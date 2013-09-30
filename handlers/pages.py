#coding=utf-8
from base import WwwBaseHdl


class PageIndexHdl(WwwBaseHdl):
    def get(self):
        globalConf = self.settings['globalConfig']
        selfHost = globalConf.get('website', 'host')
        self.render('upload.html', selfHost=selfHost)
        return