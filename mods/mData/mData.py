#coding=utf-8
import time


class mData(object):
    def __init__(self, dbConn):
        self.dbConn = dbConn
        return

    def VideoAdd(self, uid, fileKey, opsId):
        table = 'qalbum_videos'
        sql = '''
        INSERT INTO %s(uid, created_at, hash, pid) VALUES (?, ?, ?, ?)
        ''' % (table,)
        now = int(time.time())
        res = self.dbConn.execute(sql, (uid, now, fileKey, opsId))
        return res > 0

    def VideoUpdateOpsStatus(self, opsId, status, data):
        res = self.VideoAddNotify(opsId, data)
        if res:
            table = 'qalbum_videos'
            sql = '''
            UPDATE %s SET pstatus=? WHERE pid=?
            ''' % (table,)
            res = self.dbConn.execute(sql, (status, opsId))
            return res > 0
        return res

    def VideoAddNotify(self, opsId, data):
        table = 'qalbum_notify'
        sql = '''
        INSERT INTO %s(pid, data) VALUES (?, ?)
        ''' % (table,)
        res = self.dbConn.execute(sql, (opsId, data))
        return res > 0