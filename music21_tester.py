from music21 import *


s = corpus.parse('bach/bwv65.2.xml')
print (s.analyze('key'))
environment.set('musicxmlPath', '/usr/bin/musescore')
s.show()