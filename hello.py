import cv2
import numpy as np
import mediapipe as mp
import tensorflow as tf
from tensorflow.keras.models import load_model

# Taken from https://techvidvan.com/tutorials/hand-gesture-recognition-tensorflow-opencv/

"""
Initializes mediapipe
"""
# Performs the hand recognition algorithm
mpHands = mp.solutions.hands
# Configure the model
hands = mpHands.Hands(max_num_hands=3)
# Draws detected key points of hand
mpDraw = mp.solutions.drawing_utils

"""
Initialize tensorflow
"""
# Loads the gesutre recognizer model
model = load_model('mp_hand_gesture')
# f = open('gesture.names', 'r')
# classNames = f.read().split('\n')
# f.close()
# print(classNames)


"""
Read frames from webcam
"""
cap = cv2.VideoCapture(0)
while True:
    # Read each frame from webcam
    _, frame = cap.read()
    x, y, c = frame.shape
    
    # Flip frame vertically (why? can this give problems when signing?)
    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    #Get hand landmark prediction
    result = hands.process(framergb)

    """
    Detect hand keypoints
    """
    # If any hand is detected
    if result.multi_hand_landmarks:
        landmarks = []
        # Loop through each detection
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # Print(id, lm)
                # Model returns a normalized result so we multiply with frame dims.
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])
            # Drawing landmarks on frames 
            bokstavA = handslms
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
    # Show the final output
    cv2.imshow("Output", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(handslms)

