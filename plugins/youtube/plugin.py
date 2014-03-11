from bs4 import BeautifulSoup
from bot import IRCBot
import re, urllib2
def find(command):
    if re.search("https://www.youtube|http://www.youtube", command):
        return 1
    return 0

def run(irc, channel, message):
    #Get the YouTube link from the raw IRC data
    url = message.split(" ")
    url = url[3].split("//")
    url = url[1]
    reader = urllib2.urlopen("http://%s" %url)
    soup = BeautifulSoup(reader.read())
    title = soup.title.string.replace("YouTube", "https://%s" %url)
    IRCBot.sendMessage(irc, channel, title)