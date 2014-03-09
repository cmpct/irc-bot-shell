class IRCBot():

    def __init__(self, nick, user, server, channel):
        self.nick     = nick
        self.user     = user
        self.server   = server
        self.channel  = channel #Make this an array

    def output(self, data):
        print(">> Server: %s: %s" % (self.server, data))

    def sendMessage(self, channel, message):
        self.sock.send("PRIVMSG %s :%s\r\n" %(channel, message))

    def sendPacket(self, packet):
        self.sock.send(packet)

    def joinChan(self, channel):
        self.sock.send("JOIN %s\r\n" % channel)