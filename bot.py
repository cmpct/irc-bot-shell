import socket

class IRCBot():

    def __init__(self, nick, user, server, ip, channels):
        self.nick     = nick
        self.user     = user
        self.server   = server
        self.ip       = ip
        self.channels  = channels #Make this an array

    def output(self, data):
        print(">> %s: %s" % (self.server, data))

    def sendMessage(self, channel, message):
        self.sock.send("PRIVMSG %s :%s\r\n" %(channel, message))

    def sendPacket(self, packet):
        self.sock.send(packet + "\r\n")

    def joinChan(self, channel):
        self.sock.send("JOIN %s\r\n" % channel)

    def joinChannels(self):
        for channel in self.channels:
            self.joinChan(channel)

    def changeTopic(self, topic, channel):
        self.sock.send("TOPIC %s :%s\r\n" %(channel, topic))

    def sendAction(self, action, channel):
        self.sock.send("ACTION %s :%s\r\n" %(channel, action))

    def getMessage(self):
        return self.x[4]

    def splitData(self):
        self.x = self.data.split(" ")
        return self.x

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server, self.ip))
        self.sendPacket("NICK %s" %self.nick)
        self.sendPacket("USER %s %s %s :%s" %(self.user, self.user, self.user, self.user))

        while 1:
            self.data = self.sock.recv(2040)
            self.output(self.data)
            self.splitData()

            if self.x[0] == ":PING":
                self.sendPacket("PONG %s" %self.x[1])