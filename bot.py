import socket, pluginloader, thread, ssl, re

class IRCBot():

    def __init__(self, nick, user, server, ip, channels, ssl=False):
        self.nick     = nick
        self.user     = user
        self.server   = server
        self.ip       = ip
        self.channels  = channels
        self.ssl      = ssl

    def output(self, data):
        print(">>%s: %s" % (self.server, data))

    def sendPacket(self, packet):
        self.sock.send(packet + "\r\n")

    def sendMessage(self, channel, message):
        self.sendPacket("PRIVMSG %s :%s" %(channel, message))

    def joinChan(self, channel):
        self.sendPacket("JOIN %s" %channel)

    def joinChannels(self):
        for channel in self.channels:
            self.joinChan(channel)

    def changeTopic(self, topic, channel):
        self.sendPacket("TOPIC %s :%s" %(channel, topic))

    def sendAction(self, action, channel):
        self.sendPacket("ACTION %s :%s" %(channel, action))

    def handleMessage(self, message):
        channel = message.split(" ")
        channel = channel[2]
        #message = message.split(":")
        thread.start_new_thread(self.runPlugin, (message, channel))

    def runPlugin(self, message, channel):
        for plugins in pluginloader.getPlugins():
            plugin = pluginloader.loadPlugin(plugins)
            event = plugin.find(message)
            if event == 1:
                plugin.run(self, channel, message)
                break

    def splitData(self):
        self.x = self.data.split(" ")
        return self.x

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server, self.ip))
        if self.ssl == True:
            self.sock = ssl.wrap_socket(self.sock)

        self.sendPacket("NICK %s" %self.nick)
        self.sendPacket("USER %s %s %s :%s" %(self.user, self.user, self.user, self.user))

        while 1:
            self.data = self.sock.recv(2040)
            self.output(self.data)
            self.splitData()
            try:
                if re.search("PRIVMSG", self.x[1]):
                    self.handleMessage(self.data)
            except IndexError:
                pass
            try:
                if re.search("PING", self.x[0]):
                    self.sendPacket("PONG %s" %self.x[1])
                    self.joinChannels()
            except IndexError:
                pass

            try:
                if re.search(self.nick, self.x[2]):
                    self.joinChannels()
                    # THIS IS BAD
            except IndexError:
                pass