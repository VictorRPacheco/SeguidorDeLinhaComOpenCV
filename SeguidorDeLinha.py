import numpy as np
import cv2
import imageio

cap = cv2.VideoCapture(0)

while(True):

	ret, frame = cap.read()
	raw = frame.copy()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.flip(gray, 1)

	LEFT = gray[400:450, 0:213]
	CENTER = gray[400:450, 213:426]
	RIGHT = gray[400:450, 426:639]
	cv2.rectangle(gray,(0,400),(639,450),(0,255,0),3)
	cv2.rectangle(gray,(0,400),(213,450),(0,255,0),2)
	cv2.rectangle(gray,(213,400),(426,450),(0,255,0),2)
	cv2.rectangle(gray,(426,400),(639,450),(0,255,0),2)
		
	if cv2.mean(CENTER)[0] < cv2.mean(LEFT)[0] and cv2.mean(CENTER)[0] < cv2.mean(RIGHT)[0]:
		print("Frente")
		cv2.arrowedLine(gray, (319,350), (319,100), (0, 255, 0), 8)
	else:
		if cv2.mean(RIGHT)[0] < cv2.mean(LEFT)[0]:
			print("Direita")
			cv2.arrowedLine(gray, (219,300), (419,300), (0, 255, 0), 8)
		else:
			print("Esquerda")
			cv2.arrowedLine(gray, (419,300), (219,300), (0, 255, 0), 8)
			
	cv2.imshow('frame',gray)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break