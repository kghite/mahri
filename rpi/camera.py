"""
Camera stream management
"""

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 

class CameraController:

	def __init__(self):
		self.camera = PiCamera()
		self.raw_capture = PiRGBArray(self.camera)
		time.sleep(0.1)

	"""
	Capture raw camera image
	"""
	def capture_cvimage(self):
		self.camera.capture(self.raw_capture, format='bgr')
		image = self.raw_capture.array
		
		return image
 
	"""
	Capture streamable camera frame
	"""
	def capture_frame(self):
		self.camera.capture(self.raw_capture, format='bgr')
		image = self.raw_capture.array
		ret, jpeg = cv2.imencode('.jpg', image)

        return jpeg.tobytes()


if __name__ == '__main__':
	# Get test image frame
	cam = CameraController()
	cam.capture_cvimage()

	cv2.imshow('RPi Zero', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
