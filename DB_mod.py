import time
import json
import datetime
import sqlite3

def set_is_kid_home(is_kid_home):
    conn = sqlite3.connect("stationdb.sqlite3", isolation_level=None)
    
    c = conn.cursor()
    c.execute("UPDATE kid set is_kid_home=%s where id = 1" %str(is_kid_home))
    
    conn.close()

def set_where_is_kid(where_is_kid):
    conn = sqlite3.connect("stationdb.sqlite3", isolation_level=None)
    
    c = conn.cursor()
    c.execute("UPDATE kid set is_kid_home='%s' where id = 1" %where_is_kid)
    
    conn.close()

def set_is_kid_ready(is_kid_ready):
    conn = sqlite3.connect("stationdb.sqlite3", isolation_level=None)
    
    c = conn.cursor()
    c.execute("UPDATE kid set is_kid_home='%s' where id = 1" %is_kid_ready)
    
    conn.close()

def set_current_stage(current_stage):
    conn = sqlite3.connect("stationdb.sqlite3", isolation_level=None)
    
    c = conn.cursor()
    
    c.execute("UPDATE kid set current_stage='%s' where id = 1" %current_stage)
    conn.close()

def set_current_state(current_state):
    conn = sqlite3.connect("stationdb.sqlite3", isolation_level=None)
    
    c = conn.cursor()
    
    c.execute("UPDATE kid set current_state='%s' where id = 1" %current_state)
    conn.close()

    
def set_lazy_cnt(lazy_cnt):
    conn = sqlite3.connect("stationdb.sqlite3", isolation_level=None)
    
    c = conn.cursor()
    
    c.execute("UPDATE kid set lazy_cnt=%s where id = 1" %str(lazy_cnt))
    conn.close()
    
if __name__ == "__main__" : 
    set_is_kid_home(1)