import time
import fluidsynth

# First a Synth object is created to control playback.
fs = fluidsynth.Synth()
# The start() method starts audio output in a separate thread.
# fs.start()
fs.start(driver="alsa")
## Your installation of FluidSynth may require a different driver.
## Use something like:
# fs.start(driver="pulseaudio")
# fs.start(driver="alsa", midi_driver="alsa_seq")

# Got this error trying different drivers:
# fluidsynth: error: Couldn't find the requested 
# audio driver portaudio. Valid drivers are: 
# alsa, file, jack, oss, pulseaudio.

# sfid = fs.sfload("example.sf2")
sfid = fs.sfload("/usr/share/sounds/sf2/FluidR3_GM.sf2")
# program_select(track, soundfontid, banknum, presetnum)
fs.program_select(0, sfid, 0, 0)

# noteon(track, midinum, velocity)
fs.noteon(0, 60, 30)
fs.noteon(0, 67, 30)
fs.noteon(0, 76, 30)

time.sleep(1.0)

# noteoff(track, midinum)
fs.noteoff(0, 60)
fs.noteoff(0, 67)
fs.noteoff(0, 76)

time.sleep(1.0)

fs.delete()