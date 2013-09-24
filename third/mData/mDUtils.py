#coding=utf-8
import sqlite3


sqlForSqlite = [
    'DROP TABLE IF EXISTS `users`',
    '''
    CREATE TABLE `users` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `username` TEXT NOT NULL ,
        `email` TEXT NOT NULL DEFAULT "",
        `password` TEXT NOT NULL ,
        `created_at` INTEGER NOT NULL DEFAULT 0 ,
        `updated_at` INTEGER NOT NULL DEFAULT 0
    )
    ''',
    '''
    CREATE UNIQUE INDEX index_users_on_username ON users(username)
    ''',
    '''
    DROP TABLE IF EXISTS `videos`
    ''',
    '''
    CREATE TABLE `videos` (
        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `user_id` INTEGER NOT NULL DEFAULT 0 ,
        `file_size` INTEGER NOT NULL DEFAULT 0 ,
        `file_type` TEXT NOT NULL DEFAULT "" ,
        `created_at` INTEGER NOT NULL DEFAULT 0 ,
        `hash` TEXT NOT NULL DEFAULT "" ,
        `ops_status` INTEGER NOT NULL DEFAULT 0
    )
    ''',
    '''
    CREATE INDEX index_videos_on_userid ON videos(user_id)
    ''',
]


def dbInitSqlite(dbPath):
    conn = makeSqliteConn(dbPath)
    for sql in sqlForSqlite:
        conn.execute(sql)
    return


def makeSqliteConn(dbPath, isolation_level=None):
    if dbPath:
        conn = sqlite3.connect(dbPath, isolation_level=isolation_level)
        cur = conn.cursor()
        cur.execute('PRAGMA encoding = "UTF-8"')
        return cur
    return