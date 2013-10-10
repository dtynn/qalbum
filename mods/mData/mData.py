#coding=utf-8
import time


class mData(object):
    def __init__(self, dbConn):
        self.dbConn = dbConn
        return

    def VideoAdd(self, uid, fileKey, fileName, opsId):
        table = 'qalbum_videos'
        sql = '''
        INSERT INTO %s(uid, created_at, hash, pid, file_name) VALUES (?, ?, ?, ?, ?)
        ''' % (table,)
        now = int(time.time())
        res = self.dbConn.execute(sql, (uid, now, fileKey, opsId, fileName))
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

    def VideoListAll(self):
        table = 'qalbum_videos'
        sql = '''
        SELECT vid, uid, created_at, hash, file_name, pid, pstatus FROM %s ORDER BY vid DESC
        ''' % (table,)
        res = self.dbConn.query(sql)
        return res

    def VideoGetNotify(self, pid):
        table = 'qalbum_notify'
        sql = '''
        SELECT data FROM %s WHERE pid=?
        ''' % (table, )
        res = self.dbConn.get(sql, (pid,))
        return res

    def VideoGet(self, vid):
        table = 'qalbum_videos'
        sql = '''
        SELECT vid, uid, created_at, hash, file_name, pid, pstatus FROM %s WHERE vid=?
        ''' % (table,)
        res = self.dbConn.get(sql, (vid,))
        return res