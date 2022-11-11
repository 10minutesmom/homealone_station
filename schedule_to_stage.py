import time
import json
import datetime
import sqlite3


def fetch_schedule () :
    conn = sqlite3.connect("stationdb.sqlite3", isolation_level=None)
    
    c = conn.cursor()
    c.execute("SELECT schedule_uri FROM kid")
    
    dir = c.fetchone()[0]
    conn.close()
    
    f = open(dir)
    data = json.load(f)
    f.close()

    return data

def convert_schedule_to_stage(data):
    pass

if __name__ == "__main__" :   
    print(datetime.datetime.now())
    schedule_JSON = fetch_schedule()
    convert_schedule_to_stage(schedule_JSON)
    


