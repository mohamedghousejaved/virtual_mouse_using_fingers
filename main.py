import cv2 #to operate camera as input for python library
import mediapipe as mp #google library for measurements of human body and other objects
import pyautogui #to operate library of computer operations like mouse and keyboards


url='http://192.168.1.5:8080/video' #to connect camera of phone with computer using ip webcam app
cap = cv2.VideoCapture(url)

hand_detector = mp.solutions.hands.Hands()#calling files from google mediapipe database
drawing_utils = mp.solutions.drawing_utils


screen_width, screen_height = pyautogui.size() #getting size of coverage of camera sight

index_y = 0

while True:
    _, frame = cap.read() #


    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y

                if id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    print('outside', abs(index_y - thumb_y))
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    elif abs(index_y - thumb_y) < 100:
                        pyautogui.moveTo(index_x, index_y)
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)