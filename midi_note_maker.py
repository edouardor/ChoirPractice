import pygame.midi
import time
import fluidsynth

pygame.midi.init()

# fluidsynth --server --audio-driver=alsa -o audio.alsa.device=hw:0 /usr/share/sounds/sf2/FluidR3_GM.sf2
# The above line in the linux command line runs fluidsynth 
# and makes another device appear in the following inquiries. 
# It is this function that I need to figure out how to call 
# from the python script itself.  It may require the importing 
# of the fluidsynth python module, but that hasn't been 
# successfull thus far.

print (pygame.midi.get_default_output_id())

r = range(pygame.midi.get_count())

output_ids = []
for n in r:
    print (n,pygame.midi.get_device_info(n),r)
    if pygame.midi.get_device_info(n)[3] == 1:
    	output_ids.append(n)
    else:
    	pass

print (output_ids)
# When FluidSynth is 'on', it shows up as the last port of available devices.
# This tells pygame to use that last device.
fs_id_port = output_ids[-1]
print (fs_id_port)
player = pygame.midi.Output(fs_id_port)
player.set_instrument(0)
print ('Playing...')
player.note_on(64, 127)
time.sleep(1)
player.note_off(64, 127)
print ('Played')
del player
pygame.midi.quit()



# Soundcard is on card 0 device 0, or "hw:0,0"
# And the sound device that drives the HDMI port is on card 0 device 3, or "hw:0,3"

