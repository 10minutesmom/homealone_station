from apscheduler.schedulers.background import BackgroundScheduler
import state_manager
import time
import json
import datetime
import sqlite3

sched = BackgroundScheduler()

def receive_stage () :
    ts_h = str(datetime.datetime.now())[11:13]
    ts_m = str(int(int(str(datetime.datetime.now())[14:16])/10)*10)
    
    conn = sqlite3.connect("stationdb.sqlite3", isolation_level=None)
    
    c = conn.cursor()
    c.execute("SELECT stage_uri FROM kid")
    
    dir = c.fetchone()[0]
    conn.close()
    
    f = open(dir)
    data = json.load(f)
    current_stage = data['timetable'][ts_h][ts_m]['stage']
    f.close()

    return current_stage

def set_stage(current_stage):
    conn = sqlite3.connect("stationdb.sqlite3", isolation_level=None)
    
    c = conn.cursor()
    
    c.execute("UPDATE kid set current_stage='%s' where id = 1" %current_stage)
    conn.close()
    
def set_state():
    print('executed state manager')

@sched.scheduled_job('cron', hour='0-23', minute='*/10', id='req')
def req():
    print(datetime.datetime.now())
    current_stage = receive_stage ()
    set_stage(current_stage)
    time.sleep(5)
    set_state()
    
if __name__ == "__main__" : 
    sched.start()
    while True:
        time.sleep(1)   

