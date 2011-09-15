from googlevoice import Voice
from googlevoice.util import input
import urllib2
import hashlib

pageToCheck='http://www.hp.com/united-states/webos/us/en/tablet/touchpad-availability.html'
originalPageHash='dcc01cc24938082ecef01e9aa874083f' #HP touchpad hash for the learn more page
phoneNumbers = ['']
alertText = 'holy SHIT THE HP TOUCHPAD PAGE HAS CHANGED!!!'

def getPage(pageToCheck):
    page = urllib2.urlopen(pageToCheck).read()
    return page
    
def checkForPage():
    page = getPage(pageToCheck)
    pageHash = hashlib.md5(page).hexdigest()
    print "checking page hash"
    if ( pageHash != originalPageHash ):
        sendTxt()
        print alertText

def sendTxt():
    voice = Voice()
    voice.login()
    for phoneNumber in phoneNumbers:
        voice.send_sms(phoneNumber, alertText)

checkForPage()
