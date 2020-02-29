import autcommand
from command import Command
import exic
from command import Type

commands_data = [
    
    Command(
        [
            ["джарвис"]
        ],
        'triggered',
        type_= 1
    ),
    Command(
        [
            ["включи", "свет"],
            ["включить","свет"]
        ],
        b"1 -1 -1",
        type_= 0
    ),
    Command(
        [
            ["выключи", "свет"],
            ["выключить","свет"]
        ],
        b"0 -1 -1",
        type_= 0
    ),
    Command(
        [
            ["закрой", "окно"],
            ["закрыть","окно"]
        ],
        b"-1 0 -1",
        type_= 0        
    ),
    Command(
        [
            ["открой", "окно"],
            ["открыть","окно"]
        ],
        b"-1 1 -1",
        type_= 0
    ),
    Command(
        [
            ["открой", "дверь"],
            ["открыть","дверь"]
        ],
        b"-1 -1 1",
        type_= 0
    ),
    Command(
        [
            ["закрой", "дверь"],
            ["закрыть","дверь"]
        ],
        b"-1 -1 0",
        type_= 0

    ),    
        
    Command(
        [
            ["закрой", "всё"],
            ["закрыть","всё"],
            ["я","ухожу"]
        ],
        b"0 0 0",
        type_= 0

    ),
        
    Command(
        [
            ["открой", "всё"],
            ["открыть","всё"]
        ],
        b"-1 -1 0",
        type_= 0

    ),  
    Command(
        [
            ["сколько", "времени"],
            ["который", " час"],
            ["текущее", "время"]
        ],
        autcommand.get_time,
        type_= 1

    ),
    Command(
        [
            ["расскажи", "анекдот"],
            ["расскажи", "шутку"],
        ],
        autcommand.tell_joke,
        type_= 1

    ),
    Command(
        [
            ["привет"],
            ["прив"],
            ["здравствуй"],
            ["здравствуйте"]
        ],
        autcommand.say_hi,
        type_= 1
    ),
    Command(
        [
            ["погода"],
            ["какая", "погода"]
        ],
        autcommand.weather,
        type_= 1
    ), 
    Command(
        [
            ["музыка"],
            ["включи","музыку"],
            ["давай","пошумим"] 
        ],
        exic.music_on,
        type_= 2
    ),
    Command(
        [
            ["открой","гугл"],
            ["открой","браузер"],
            ["браузер"],
            ["открыть","браузер"],
            ["открыть","гугл"]
        ],
        exic.brovser_on,
        type_= 2
    ),   
    Command(
        [
            ["как","дела"],
            ["как", "сам"]
        ],
        autcommand.i_m_ok,
        type_= 1
    ), 
    Command(
        [
            ["молодец"],
        ],
        autcommand.well_done,
        type_= 1
    ),
]

class Commands:
    def __init__(self, commads=commands_data):
        self.commands = commads

    def get(self, user_text):
        for cmd in self.commands:
            for keys in cmd.get_keywords():
                count = 0
                fkeyword = []
                for key in keys:
                    if key in user_text:
                        if key in user_text and key not in fkeyword:
                            count += 1
                            fkeyword.append(key)
                if count == len(keys):
                    return cmd.get_command(), cmd.get_type()

        return autcommand.i_not_understand, None