import time
import cv2
import numpy as np
import pickle
import serial
print(cv2.__version__)

class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2):
        self.hands=self.mp.solutions.hands.Hands(False,maxHands)
    def Marks(self,frame):
        myHands=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands

def findDistances(handData):
    distance_matrix = np.zeros([len(handData), len(handData)], dtype='float')
    palm_size = ((handData[0][0] - handData[9][0])**2 + (handData[0][1] - handData[9][1])**2)**(1./2.)
    for y in range(0, len(handData)):
        for x in range(0, len(handData)):
            distance_matrix[y][x] = (((handData[y][0] - handData[x][0])**2 + (handData[y][1] - handData[x][1])**2)**(1./2.)) / palm_size
    return distance_matrix

def find_error(gesture_matrix, unknown_matrix, key_points):
    error = 0
    for y in key_points:
        for x in key_points:
            error = error + abs(gesture_matrix[y][x] - unknown_matrix[y][x])
    return error

arduino_data = serial.Serial('com3', 9600)

time.sleep(1)
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
findHands=mpHands(1)

key_points = [0,4,5,9,13,17,8,12,16,20]
tolerance = 10
cmd = 'junk'
with open('my_Close.pkl', 'rb') as f:
    known_gesture = pickle.load(f)
while True:
    ignore,  frame = cam.read()
    handData=findHands.Marks(frame)
    if handData != []:        
        unknown_gesture = findDistances(handData[0])
        error_value = find_error(known_gesture, unknown_gesture, key_points)
        error_value = int(error_value)  # round the number
        if error_value < tolerance:
            print('tutup')
            cmd = 'tutup\r'
        else:
            cmd = 'buka\r'
            print('buka')
    for hand in handData:
        for ind in key_points:
            cv2.circle(frame,hand[ind],10,(255,0,255),3)
    arduino_data.write(cmd.encode())
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
