def find(command):
    triggers = ["hello", "hi", "hey"]
    for cmd in triggers:
        if cmd == command.strip():
            return 1
    return 0

def run():
    print "This works so far, now to communicate with IRC through the class.."