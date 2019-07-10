"""
Light Controller
"""

import board
import neopixel


class LightsController:
	
	def __init__(self, num_pixels):
		self.num_pixels = num_pixels
		self.pixels = neopixel.NeoPixel(board.D18, num_lights)

	"""
	Set all pixels to rgb tuple value
	"""
	def fill_lights(self, rgb):
		self.pixels.fill(rgb)

	"""
	Set pixels to list of rgb tuple values
	"""
	def set_pixels(self, rgbs):
		for i in range(len(num_pixels)):
			self.pixels[i] = rgbs[i]


if __name__ == '__main__':
	lights = LightsController(5)
	lights.fill_lights((255, 0, 0))
