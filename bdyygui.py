#!/usr/bin/env python3
#-*- coding:utf8 -*-
# Power by pHJ 2019-10-12 01:11
import PySimpleGUI as sg
from aip import AipSpeech
#""" APPID AK SK """
APP_ID = ''#填入自己的百度API
API_KEY = ''#填入自己的百度API_KEY
SECRET_KEY=''#填入自己的百度SECRET_KEY
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 
layout = [ [sg.Text('百度文字转声音生成mp3，')],
            [sg.Text('输入所需转换的文字'), sg.Multiline(default_text='', size=(60, 3))],#sg.InputText()],#$
            
            
            [sg.Text('Enter spd(语速)'),
            sg.Slider(range=(1, 15), orientation='h', size=(20, 20), default_value=5)],
             [sg.Text('Enter pit(音调)'),
            sg.Slider(range=(1, 15), orientation='h', size=(20, 20), default_value=5)],
            
              [sg.Text('Enter vol(音量)'),
            sg.Slider(range=(1, 15), orientation='h', size=(20, 20), default_value=5)],
               [sg.Text('Enter per(角色)'),
            sg.Slider(range=(0, 4), orientation='h', size=(20, 20), default_value=3)],
                [sg.Text('0=女生，1=男生，3=情感男声，4=情感女生。')],
            [sg.Text('文件名')],
            [sg.Input(default_text='1')],
            [sg.Button('Ok'), sg.Button('Cancel')],
           
            
            ]
            
# 
window = sg.Window('百度文字转声音', layout)

# 
while True:
    event, values = window.read()
    if event in (None, 'Cancel'): 
        break
   
   
    content=str(values[0])
    result  = client.synthesis(content,'zh',1,{'spd':values[1], 'pit':values[2],'vol': values[3],'per':values[4]})
    if not isinstance(result, dict):
        with open(values[5]+'.mp3', 'wb') as f:#文件 名默认为1.mp3
            f.write(result)
    #print ('ok')
    sg.Popup('已完成')
window.close()
