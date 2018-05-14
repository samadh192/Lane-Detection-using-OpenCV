import cv2
import numpy as np


cap=cv2.VideoCapture('project_video.mp4')
k=1

while True:
	ret,frame=cap.read()


	rows,cols = frame.shape[0:2]
	bottom_left  = [cols*0.1, rows*0.95]
	top_left     = [cols*0.45, rows*0.6]
	bottom_right = [cols*1, rows*0.92]
	corner		 = [cols*1, rows*0.65]
	top_right    = [cols*0.7, rows*0.6]

	vertices = np.array([[bottom_left, top_left, top_right, corner,bottom_right]], dtype=np.int32)

	mask = np.zeros_like(frame)
	if len(mask.shape)==2:
		cv2.fillPoly(mask, vertices, 255)
	else:
		cv2.fillPoly(mask, vertices, (255,)*mask.shape[2])
	roi=cv2.bitwise_and(frame,mask)

	hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)
	lower_yellow=np.array([8,152,205])
	upper_yellow=np.array([42,252,255])
	lower_white=np.array([2,0,200])
	upper_white=np.array([46,21,255])
	yellow=cv2.inRange(hsv,lower_yellow,upper_yellow)
	white=cv2.inRange(hsv,lower_white,upper_white)

	yellow_and_white=yellow+white



	#gray=cv2.cvtColor(yellow_and_white,cv2.COLOR_BGR2GRAY)
	blur=cv2.GaussianBlur(yellow_and_white, (3, 3), 0)
	canny_edge=cv2.Canny(blur,50,150)

	cv2.namedWindow('Original',cv2.WINDOW_NORMAL)
	cv2.namedWindow('Canny Edge',cv2.WINDOW_NORMAL)
	cv2.namedWindow('ROI',cv2.WINDOW_NORMAL)
	#cv2.namedWindow('Final ROI',cv2.WINDOW_NORMAL)


	#cv2.imshow('Canny Edge',canny_edge)
	#cv2.imshow('Mask',yellow_and_white)
	#mask = np.zeros_like(frame)
	#cv2.imshow('Mask',mask)

	#rows,cols,channels=image.shape


	#final_roi=cv2.bitwise_and(canny_edge,canny_edge,mask=roi)

	#cv2.imshow('Final ROI',final_roi)
	cv2.imshow('ROI',roi)

	#print canny_edge.shape
	#print mask.shape

	lines=cv2.HoughLinesP(canny_edge,rho=1,theta=np.pi/180,threshold=10,minLineLength=20,maxLineGap=1000)

	#for line in lines:
	#	print line
	#	print "----"

	#lines = cv2.HoughLines(canny_edge,1,np.pi/180,200)

	#lines = cv2.HoughLinesP(canny_edge,1,np.pi/180,100,minLineLength=10,maxLineGap=300)
	for x1,y1,x2,y2 in lines[0]:
		m=(x2-x1)/(y2-y1)
		c=y1-m*x1
		cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),20)
		if m>0:
			cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),20)



	cv2.imshow('Canny Edge',canny_edge)
	cv2.imshow('Original',frame)

	#print m
	#print c

	if cv2.waitKey(20) & 0xFF ==27:
		break
cap.release()
cv2.destroyAllWindows()
