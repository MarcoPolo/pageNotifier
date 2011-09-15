import urllib2
import hashlib

pageurl = raw_input('paste the page url here: ')
page = urllib2.urlopen(pageurl).read()
pageHash = hashlib.md5(page).hexdigest()
print pageHash
