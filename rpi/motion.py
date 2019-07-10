"""
Motion Controllers
"""

import RPi.GPIO as GPIO
import time


"""
Servo management and positional control
"""
class Servo:
	
	def __init__(self, name, pin):
		self.name = name
		self.position = None

		GPIO.setup(pin, GPIO.OUT)
		self.pwm = GPIO.PWM(pin, 50)
	
	def set(self, angle):
		duty = angle / 180 + 1
		self.pwm.ChangeDutyCycle(duty)
		self.position = angle
		# TODO: Need to wait for angle to reach?


"""
Robot motion control
"""
class MotionController:
	
	def __init__(self, robot_id):
		self.robot_id = robot_id
	
	"""
	Proportional sumultaneous servo motion
	All servos start and stop motion at the same time based on most granular
	"""
	def ps_move(servos, angles):
		motion = {}

		# Create servo step arrays
		steps = []
		dists = []
		for servo, angle in zip(servos, angles):
			if servo.position > angle: 
				steps.append(list(range(servo.position, angle, -1)))
			else: steps.append(list(range(servo.position, angle)))
			dists.append(abs(servo.position - angle))
		max_dist = max(dists)

		# Map position arrays to longest
		for servo, step_list in zip(servos, steps):
			if step_list: # Handle moving to same position
				motion[servo] = [step_list[i * len(step_list) // max_dist] 
									for i in range(max_dist)]

		# Move the servos by step
		# TODO: Check for interruption
		for i in range(max_dist):
			for servo in motion.keys():
				servo.set(motion[servo][i])


if __name__ == '__main__':
	# Test servo position settings
	tilt_servo = Servo('tilt', 14)
	rotation_servo = Servo('rotation', 15)

	angles = [0, 45, 90, 180]
	for angle in angles:
		tilt_servo.set(angle)
		rotation_servo.set(angle)
		time.sleep(2)

	# Test proportional servo control
	mc = MotionController('mahri')
	mc.ps_move([tilt_servo, rotation_servo], [45, 180])
