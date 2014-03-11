from bot import IRCBot
def find(command):
    triggers = ["hello", "hi", "hey"]
    for cmd in triggers:
        if cmd == command.strip():
            return 1
    return 0

def run(irc, channel):
    IRCBot.sendMessage(irc, channel, "Hello")