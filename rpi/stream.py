"""
Read from server stream to manage robot, send sensor stream back
Manage robot state in reference to interaction tempo
"""

class Stream:

	def __init__(self):
		self.tempo = None
		self.server = None

	def set_tempo(self, bpm):
		pass

	def get_update(self):
		pass

	def set_state(self, state):
		pass

	def send_update(self):
		pass
