# -*- coding: utf-8 -*-

import sys
import subprocess
import time
from runfs import Runfs

def main(song):
	fs = Runfs()
	fs.server('alsa')
	lmplay(song)

def lmplay(song):
	args = []
	args = ['aplaymidi', '-p', '128:0', song]
	# aplaymidi -p 128:0 song.mid
	print (args)
	global mp
	mp = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf-8')#, text=True)
	# (sout,serr) = mp.communicate()
	# for line in sout.split('\n'):
		# print (line)
	time.sleep(10)
	fs.quit()
# Need to check if song is done, then fs.quit()

if __name__ == "__main__":
	if(len(sys.argv) != 2):
		print ("##### ERROR: Please provide a file name of midi song")
		print ("***** Example: python3 'lmplayer.py' 'song.mid'")
		print ("Exiting...")
		sys.exit()
	song = sys.argv[1]
	main(song)