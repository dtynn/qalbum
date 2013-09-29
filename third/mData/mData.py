#coding=utf-8
import time


class mData(object):
    def __init__(self, dbConn):
        self.dbConn = dbConn
        return

    def VideoAdd(self, uid, fileKey, opsId):
        table = 'qalbum_videos'
        sql = '''
        INSERT INTO %s(uid, created_at, hash, ops_id) VALUES (?, ?, ?, ?)
        ''' % (table,)
        now = int(time.time())
        res = self.dbConn.execute(sql, (uid, now, fileKey, opsId))
        return res > 0

    def VideoUpdateOpsStatus(self, opsId, status=1):
        table = 'qalbum_videos'
        sql = '''
        UPDATE %s SET status=? WHERE ops_id="?"
        ''' % (table,)
        res = self.dbConn.execute(sql, (status, opsId))
        return res > 0