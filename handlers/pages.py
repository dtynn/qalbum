#coding=utf-8
from base import WwwBaseHdl


class PageIndexHdl(WwwBaseHdl):
    def get(self):
        globalConf = self.settings['globalConfig']
        selfHost = globalConf.get('website', 'host')
        self.render('upload.html', selfHost=selfHost)
        return


class PageListHdl(WwwBaseHdl):
    def get(self):
        mDataMod = self.settings['mods']['mData']
        videoList = mDataMod.VideoListAll()
        self.ajax_finish(videoList)
        return


class PageNotifyHdl(WwwBaseHdl):
    def get(self):
        pid = self.get_argument('pid')
        mDataMod = self.settings['mods']['mData']
        if pid:
            notify = mDataMod.VideoGetNotify(pid)
            if notify:
                self.write(notify)
        return


class PagePlayerHdl(WwwBaseHdl):
    def get(self):
        self.render('player.html')
        return