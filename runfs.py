import subprocess

# print (dir(subprocess))


class runfs:
	def via_alsa(self):

		args = ['fluidsynth', '--server', '--audio-driver=alsa', '-o', 'audio.alsa.device=hw:0', '/usr/share/sounds/sf2/FluidR3_GM.sf2']
		print (args)
		myprocess = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf-8')#, text=True)
		# (sout,serr) = myprocess.communicate()
		# for line in sout.split('\n'):
			# print (line)
		# print (p)

		time.sleep(1)

	def via_jackd(self):

		pass #do later

	def quit(self):
		myprocess.communicate(input='quit')

	def show_ports(self):

		p2 = subprocess.run(['aplaymidi', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, encoding='utf-8')#, text=True)
		pout = p2.stdout
		for line in pout.split('\n'):
			print (line)

# fluidsynth --server --audio-driver=alsa -o audio.alsa.device=hw:0 /usr/share/sounds/sf2/FluidR3_GM.sf2
# The above line in the linux command line runs fluidsynth 
# and makes another device appear in the following inquiries. 
# It is this function that I need to figure out how to call 
# from the python script itself.  It may require the importing 
# of the pyfluidsynth python module, but that hasn't been 
# successfull thus far.

# Optionally:
# fluidsynth --server --audio-driver=jack --connect-jack-outputs /usr/share/sounds/sf2/FluidR3_GM.sf2
# Uses jackd as the driver vs alsa.

# What is for?
# jackd -d alsa --device hw:0 --rate 44100 --period 128

# The following only works if done in order. Why?
# export JACK_PLAY_CONNECT_TO=system:playback_%d
# jack-play test.wav


# Soundcard is on card 0 device 0, or "hw:0,0"
# And the sound device that drives the HDMI port is on card 0 device 3, or "hw:0,3"