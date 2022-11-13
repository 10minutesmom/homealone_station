import time
import json
import datetime
import sqlite3
import DB_fetch
import DB_mod
import remote_control

stage_dic = {'Not_in_home':'Not_in_home',
'No_schedule':'No_schedule',
'Safety_margin':'Safety_margin',
'Need_to_ready':'Need_to_ready',
'Move':'Move',
'Pause':'Pause'}

state_dic = {
'Hibernation_state' : 'Hibernation_state',
'Lazy_state': 'Lazy_state',
'Alert_state' :'Alert_state',
'Emergency_state' :'Emergency_state'
}

def state_reaction():
    cur_is_kid_home = bool(DB_fetch.get_is_kid_home)
    cur_where_is_kid = DB_fetch.get_where_is_kid
    cur_is_kid_ready = DB_fetch.get_is_kid_ready
    
    if (DB_fetch.get_current_state() == state_dic['Hibernation_state']):
        print('current state is : %s' %state_dic['Hibernation_state'])
        DB_mod.set_lazy_cnt(0)
        print("lazy_cnt = ",DB_fetch.get_lazy_cnt())
        
    elif (DB_fetch.get_current_state() == state_dic['Lazy_state']):
        print('current state is : %s' %state_dic['Lazy_state'])
        print("lazy_cnt = ",DB_fetch.get_lazy_cnt())
        if(DB_fetch.get_lazy_cnt()%3 == 0):
            remote_control.send_direction()#update is_kid_home, where_is_kid,is_kid_ready
            DB_mod.set_lazy_cnt(DB_fetch.get_lazy_cnt()+1)
            return 0
        DB_mod.set_lazy_cnt(DB_fetch.get_lazy_cnt()+1)  
        
    elif (DB_fetch.get_current_state() == state_dic['Alert_state']):
        print('current state is : %s' %state_dic['Alert_state'])
        DB_mod.set_lazy_cnt(0)
        print("lazy_cnt = ",DB_fetch.get_lazy_cnt())
        remote_control.send_direction()#update is_kid_home, where_is_kid,is_kid_ready
    
    elif (DB_fetch.get_current_state() == state_dic['Emergency_state']):
        print('current state is : %s' %state_dic['Emergency_state'])
        DB_mod.set_lazy_cnt(0)
        print("lazy_cnt = ",DB_fetch.get_lazy_cnt())
        remote_control.send_direction()#update is_kid_home, where_is_kid,is_kid_ready

def state_manager():
    current_stage = DB_fetch.get_current_stage()
    
    cur_is_kid_home = bool(DB_fetch.get_is_kid_home())
    cur_where_is_kid = DB_fetch.get_where_is_kid()
    cur_is_kid_ready = DB_fetch.get_is_kid_ready()

    print( 'cur_is_kid_home : %s\ncur_where_is_kid : %s\ncur_is_kid_ready : %s\n'%(cur_is_kid_home,cur_where_is_kid,cur_is_kid_ready))
    
    if (current_stage == stage_dic['Not_in_home']):
        DB_mod.set_current_state(state_dic['Hibernation_state'])
        
    elif (current_stage == stage_dic['No_schedule']):
        
        if(cur_is_kid_home == True):
            DB_mod.set_current_state(state_dic['Lazy_state'])
            state_reaction()
        else:
            DB_mod.set_current_state(state_dic['Alert_state'])
            state_reaction()
            
    # elif (current_stage == stage_dic['Safety_margin']):
    #     print('current state is : ',stage_dic['Safety_margin'])
    #     get_current_stage() = state_dic['Hibernation_state']
    #     play_sound()
    
    # elif (current_stage == stage_dic['Need_to_ready']):
    #     print('current state is : ',stage_dic['Need_to_ready'])
        
    #     remote_control.send_direction()#update is_kid_home, where_is_kid
        
    #     if(cur_is_kid_home == True):
    #         get_current_stage() = state_dic['Lazy_state']
    #         state_reaction(current_status)
    #     else:
    #         get_current_stage() = state_dic['Alert_state']
    #         state_reaction(current_status)
        
    # elif (current_stage == stage_dic['Move']):
    #     print('current state is : ',stage_dic['Move'])
    #     remote_control.send_direction()#update is_kid_home, where_is_kid
        
    # elif (current_stage == stage_dic['Pause']):
    #     pass