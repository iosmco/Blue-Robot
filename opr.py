import cv2
import math
import time
import numpy as np

Xposition = 90
Yposition = 90

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def remap(value_to_map, new_range_min, new_range_max, old_range_min, old_range_max):

    remapped_val = (value_to_map - old_range_min) * (new_range_max - new_range_min) / (old_range_max - old_range_min) + new_range_min
    if(remapped_val>new_range_max):
        remapped_val = new_range_max
    elif (remapped_val < new_range_min):
        remapped_val = new_range_min

    return remapped_val

def find_face(image_to_check, max_target_distance):
    gray = cv2.cvtColor(image_to_check, cv2.COLOR_BGR2GRAY) #convert image to black and white
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)     #look for faces


    if len(faces) >= 1: #if face(s) detected
        faces = list(faces)[0] #if several faces found use the first one

        x = faces[0]
        y = faces[1]
        w = faces[2]
        h = faces[3]

        center_face_X = int(x + w / 2)
        center_face_Y = int(y + h / 2)
        height, width, channels = image_to_check.shape

        distance_from_center_X = (center_face_X - width/2)/220 # why? can't remember why I did this
        distance_from_center_Y = (center_face_Y - height/2)/195 # why?

        target_distance = math.sqrt((distance_from_center_X*220)**2 + (distance_from_center_Y*195)**2) # calculate distance between image center and face center

        if target_distance < max_target_distance :#set added geometry colour
            locked = True
            color = (0, 255, 0)
        else:
            locked = False
            color = (0, 0, 255)


        cv2.rectangle(image_to_check,(center_face_X-10, center_face_Y), (center_face_X+10, center_face_Y),    #draw first line of the cross
                      color, 2)
        cv2.rectangle(image_to_check,(center_face_X, center_face_Y-10), (center_face_X, center_face_Y+10),    #draw second line of the cross
                      color,2)

        cv2.circle(image_to_check, (int(width/2), int(height/2)), int(max_target_distance) , color, 2)    #draw circle

        return [True, image_to_check, distance_from_center_X, distance_from_center_Y, locked]

    else:
        return [False]

def find_color(image_to_check, max_target_distance):
    
    global Xposition, Yposition

    hsv = cv2.cvtColor(image_to_check, cv2.COLOR_BGR2HSV)
    red_lower = np.array([161, 155, 84], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    mask = cv2.inRange(hsv, red_lower, red_upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) >= 1:
        contours = sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
        rows, cols, _ = image_to_check.shape
        center_x = int(rows / 2)
        center_y = int(cols / 2)
        
        

        for cnt in contours:
            color = (0, 0, 255)
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.rectangle(image_to_check, (x, y), (x + w, y + h), color, 2)
            # text = "x = "+str(x)+"y = "+str(y)
            # cv2.putText(image_to_check, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.50, color)
            #////////////////////////////////////////////////////////////////////
            mdm_x = int((x + x+w)/2)
            mdm_y = int((y + y+h)/2)
            #////////////////////////////////////////////////////////////////////
            cv2.line(image_to_check, (mdm_x,0),(mdm_x,1100),color,2)
            # text2 = "mediumX = " + str(mdm_x)
            # cv2.putText(image_to_check, text2, (0, 1100), cv2.FONT_HERSHEY_SIMPLEX, 0.50, color)
            #////////////////////////////////////////////////////////////////////
            cv2.line(image_to_check, (0, mdm_y), (1100, mdm_y), color, 2)
            # text3 = "mediumY = " + str(mdm_y)
            # cv2.putText(image_to_check, text3, (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.50, color)

            # ////////////////////////////////////////////////////////////////////
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            medium_x = int(x+5)
            medium_y = int(y+5)

            v=2
            m=45

            if medium_x > center_x + m:
                Xposition += v
                if Xposition>= 180:
                    Xposition = 180

            if medium_x < center_x - m:
                Xposition -= v
                if Xposition < 0:
                    Xposition = 0
            #######################################
            if medium_y > center_y + m:
                Yposition += v
                if Yposition>= 180:
                    Yposition = 180


            if medium_y < center_x - m:
                Yposition -= v
                if Yposition < 0:
                    Yposition = 0
            break
        
        return [True, image_to_check, Xposition, Yposition, True]

    else:
        return[False]
