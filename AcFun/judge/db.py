#!/usr/bin/env python
# encoding: utf-8

import config
import MySQLdb
import logging
import time, types

def execute_sql(sql):
    db = None
    while True:
        try:
            db = MySQLdb.connect(config.db_host, config.db_user, config.db_password,
                config.db_name, charset = config.db_charset)
        except:
            logging.error("can not connect Mysql")
            time.sleep(1)

    cursor = db.cursor()
    try:
        if type(sql) == types.StringType:
            cursor.execute(sql)
        elif type(sql) == types.ListType:
            for each in sql:
                cursor.execute(each)

    except MySQLdb.OperationalError, e:
        logging.error(e)
        cursor.close()
        db.close()
        return False

    con.commit()
    data = cur.fetchall()
    cursor.close()
    db.close()
    return data
