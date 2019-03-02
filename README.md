# Lane-Detection-using-OpenCV
This is a basic python script to detect lanes on a sample video of a road.

Program Description

-Create an ROI so that only the part of the road which is required is evaluated so that disturbances like trees and railings are avoided

-Create a mask to get only the yellow and white parts of the road because the markings on the road are in white and yellow.

-To create the above givem mask convert colour code to hsv and add appropriate hues for yellow and white.

-Now we use canny edge detection to detect the lines and before that apply gaussian blur to smoothen out the lines so it becomes easy to detect.

-Now use HoughLines function to detect lines and draw them.

-Show the final video.
