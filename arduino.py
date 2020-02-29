import serial


class Arduino:

    def __init__(self, com, name):
        self.name = name
        self.s = serial.Serial(com, 9600)
        # self.speeds = ['1200','2400', '4800', '9600', '19200', '38400', '57600', '115200']

    def send(self, command):
        self.s.write(command)
        print('Send to {} -> {}'.format(self.name, command))

    def recive(self):
        pass
