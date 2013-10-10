#coding=utf-8
from base import WwwBaseHdl
from tornado.httpclient import HTTPError


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
        self.write(videoList)
        #self.render('list_all.html', videoList=videoList)
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
        try:
            vid = int(self.get_argument('vid'))
        except (HTTPError, ValueError, TypeError):
            self.write('404')
            return
        mDataMod = self.settings['mods']['mData']
        res = mDataMod.VideoGet(vid)
        if res:
            etag = res['hash']
            globalConf = self.settings['globalConfig']
            domain = globalConf.get('qiniu', 'domain')
            self.render('player.html', domain=domain, etag=etag)
            return
        self.write('404')
        return