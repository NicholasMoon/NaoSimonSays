import cv2
import mediapipe as mp
import numpy as np
#from mp_Webcam import mp_holistic
from PIL import Image
import math


def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    print("angle in getangle - ", ang)
    return ang


def eval_rlh(file = 'z.png'):       # Evaluate pose - raise left hand
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    with mp_pose.Pose(
            static_image_mode=True, min_detection_confidence=0.5) as pose:
        image = cv2.imread(file)
        image_height, image_width, _ = image.shape
        # Convert the BGR image to RGB before processing.
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # Draw pose landmarks on the image.
        annotated_image = image.copy()

        mp_drawing.draw_landmarks(
            annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.imwrite('test1.png', annotated_image)
        lshoulder =  results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * image_height
        lelbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y * image_height
        lwrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * image_height

        if lelbow<lshoulder or lwrist<lshoulder: # if elbow or wrist is above the shoulder
            pose_result = 'Y'
        else :
            angle = getAngle((results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x * image_width,
                          results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * image_height)
                         , (results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x * image_width,
                            results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y * image_height)
                         , (results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x * image_width,
                            results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * image_height))
            if abs(angle)>0 and abs(angle)<90:
                pose_result = 'Y'
            else:
                pose_result = 'N'
        return pose_result

def eval_rrh(file = 'z.png'):       #evaluate pose - raise right hand
    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    with mp_pose.Pose(
            static_image_mode=True, min_detection_confidence=0.5) as pose:
        image = cv2.imread(file)
        image_height, image_width, _ = image.shape
        # Convert the BGR image to RGB before processing.
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        # Draw pose landmarks on the image.
        annotated_image = image.copy()
        mp_drawing.draw_landmarks(
            annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.imwrite('test1.png', annotated_image)
        rshoulder =  results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * image_height
        relbow = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y * image_height
        rwrist = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * image_height


        if relbow<rshoulder or rwrist<rshoulder: # if elbow or wrist is above the shoulder
            pose_result = 'Y'
        else :
            angle = getAngle((results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * image_width,
                          results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y * image_height)
                         , (results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x * image_width,
                            results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y * image_height)
                         , (results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * image_width,
                            results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y * image_height))
            print(angle)
            if abs(angle)>0 and abs(angle)<90:
                pose_result = 'Y'
            else:
                pose_result = 'N'
        return pose_result

#test = eval_rlh('Images/BH7.png')
#print(test)

pose_result = 'Z'
input_file = 'input.png'
with open("session.txt", "r") as file:
    first_line = file.readline()
    for last_line in file:
        pass
    
result = 'Could not calculate'
if last_line == 'D':
    if (eval_rrh(input_file) == 'Y' or eval_rlh(input_file) == 'Y'):
        result = 'N'
    else:
        result = 'Y'
elif last_line == 'L':
    print('RLH image')
    result = eval_rlh(input_file)
else:
    if last_line == 'R':
        print('RRH image')
        result = eval_rrh(input_file)
    else:
        if last_line == 'B':
            print('RBH image')
            if eval_rlh(input_file)+eval_rrh(input_file) == 'YY':
                result = 'Y'
            else:
                result = 'N'
                


print(result)

with open('output.txt', 'a') as outfile:
    outfile.write('\n' + result)