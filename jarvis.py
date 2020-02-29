import time
import os
from arduino import Arduino
from commands import Commands
from newvoice import Voice
from commands import Type
from command import Command

offline = False
v = Voice()
arduino_one = None
c = Command

try:
    arduino_one = Arduino('COM4', "Arduino")
except Exception:
    offline = True
com_handler = Commands()

os.startfile('C:/Program Files/Rainmeter/Rainmeter.exe')

# запущено 
#v.say("Вас приветствует голосовой помощник джарвис, полностью готов к работе")


while True:
    time.sleep(1)
    stuck = True
    while stuck:
        wait_trigger = v.hear(say_mode=True)
        command, type_ = com_handler.get(wait_trigger)
        stuck = (command != 'triggered') 

    answer = v.hear("да, сэр")
    command, type_ = com_handler.get(answer)

    if type_ == Type.answer:
        com = command()
        v.say (com) 
    elif type_ == Type.arduino:
        if not offline:
            v.say('секунду')
            time.sleep(1)
            arduino_one.send(command)
        else:
            v.say('к сожалению, ардуино не подключена, автономный режим')
    elif type_ == Type.exic :
        command()
    else:
        resp = command()
        v.say(resp)
    
        print(resp)