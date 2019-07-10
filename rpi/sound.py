"""
Sound I/O Controller
"""

import os
import time
import speakerphat


"""
Microphone input stream and text management
"""
class MicrophoneController:

	def __init__(self):
		pass


"""
Output music and robot sounds
"""
class SpeakerController:
	
	def start_mp3(self, filepath):
		os.system('omxplayer -o local %s &', filepath)
		speakerphat.clear()
		for x in range(10):
			speakerphat.set_led(x, 255 / (x+1))
		speakerphat.show()

	def pause_mp3(self):
		os.system('dbuscontrol.sh pause')
		for x in range(10):
			speakerphat.set_led(x, 0)
		speakerphat.show()