#coding=utf-8
from base import WwwBaseHdl
import json
from qiniu import conf as qConf, rs as qRs


class ApiUpTokenHdl(WwwBaseHdl):
    def get(self):
        globalConf = self.settings.get['globalConfig']
        accessKey = globalConf.get('qiniu', 'accesskey')
        secretKey = globalConf.get('qiniu', 'secretkey')
        bucket = globalConf.get('qiniu', 'bucket')
        selfHost = globalConf.get('website', 'host')
        qConf.ACCESS_KEY = accessKey
        qConf.SECRET_KEY = secretKey
        policy = qRs.PutPolicy(bucket)
        policy.callbackUrl = '%s/api/q_callback' % (selfHost,)
        policy.callbackBody = 'etag=$(etag)&opsId=$(persistentId)'
        policy.persistentOps = 'avthumb/video_240k'
        policy.persistentNotifyUrl = '%s/api/q_notify' % (selfHost,)
        uploadToken = policy.token()
        self.ajax_result(0, 0, data=uploadToken)
        return


class ApiUpCallbackHdl(WwwBaseHdl):
    def post(self):
        etag = self.get_argument('etag', '')
        opsId = self.get_argument('opsId', '')
        if etag and opsId:
            uid = 0
            mDataMod = self.settings['mods']['mData']
            res = 0 if mDataMod.VideoAdd(uid, etag, opsId) else 1
            self.ajax_result(1, res)
            return
        self.ajax_result(1, 1)
        return


class ApiPersistentNotifyHdl(WwwBaseHdl):
    def post(self):
        mimeType = 'application/json'
        if self.request.headers.get('Content-Type', '') == mimeType:
            data = self.request.body
            dataObj = json.loads(data)
            pid = dataObj.get('id')
            if pid:
                mDataMod = self.settings['mods']['mData']
                res = 0 if mDataMod.VideoUpdateOpsStatus(opsId=pid) else 1
                self.ajax_result(2, res)
                return
        self.ajax_result(2, 1)
        return