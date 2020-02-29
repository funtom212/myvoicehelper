class Type:
    arduino = 0
    answer = 1
    exic = 2

class Command:
    def __init__(self, key_words, command, autonomic=False, type_ = Type.arduino):
        self.key_words = key_words
        self.command = command
        self.autonomic = autonomic
        self.type_ = type_

    def get_keywords(self):
        return self.key_words

    # создать функцию get_command
    def get_command(self):
        return self.command

    def get_autonomic(self):
        return self.autonomic
    
    def get_type(self):
        return self.type_
