import RPi.GPIO as GPIO
import time
import readchar
import cv2

Motor_R1_Pin = 16
Motor_R2_Pin = 18
Motor_L1_Pin = 11
Motor_L2_Pin = 13
t = 0.5


GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor_R1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_R2_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L1_Pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(Motor_L2_Pin, GPIO.OUT, initial=GPIO.LOW)

def stop():
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)

def forward():
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
    time.sleep(t)
    stop()

def backward():
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, True)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, True)
    time.sleep(t)
    stop()

def turnRight():
    GPIO.output(Motor_R1_Pin, True)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, False)
    GPIO.output(Motor_L2_Pin, False)
    time.sleep(t)
    stop()

def turnLeft():
    GPIO.output(Motor_R1_Pin, False)
    GPIO.output(Motor_R2_Pin, False)
    GPIO.output(Motor_L1_Pin, True)
    GPIO.output(Motor_L2_Pin, False)
    time.sleep(t)
    stop()

if __name__ == "__main__":
	try:

		fullbody_cascade=cv2.CascadeClassifier('cars.xml')
		cap=cv2.VideoCapture(0)
	
		if not cap.isOpened():
			print('cannot opened camera')
			exit()
		while True:
			ret, frame=cap.read()
			if not ret:
				print('cannot recieve frame')
				exit()
			frame=cv2.resize(frame,(300,300))
			#gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
			#gray=cv2.medianBlur(gray,5)
			fullbody=fullbody_cascade.detectMultiScale(frame)
		
			if len(fullbody)>0:	#if got the body
				print('forward')
				forward()

			else:
				print('find people')
				turnRight()
				#time.sleep(2)

			if cv2.waitKey(1)==ord("q"):
				print('quit')
				GPIO.cleanup()
				break
		cap.release()
		cv2.destroyAllWindows()
	except KeyboardInterrupt:
		print('quit')
		GPIO.cleanup()
