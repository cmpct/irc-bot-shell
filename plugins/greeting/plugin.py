from bot import IRCBot
def find(command):
    message = command.split(":")
    triggers = ["hello", "hi", "hey"]
    for cmd in triggers:
        if cmd == message[2].strip():
            return 1
    return 0

def run(irc, channel, message):
    IRCBot.sendMessage(irc, channel, "Hello")