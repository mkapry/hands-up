import cv2
import math
import numpy as np
import mediapipe as mp

def detecter(path):
    '''Распознает ключевые точки по видео
    На вход:
        путь до видео в формате строки
    На выход: 
        3D координаты ключевых точек в виде трех списков 
        и список названий ключевых точек 
    '''
    mp_hands = mp.solutions.hands
    x_coord=[]
    y_coord=[]
    z_coord=[]
    cap = cv2.VideoCapture(path)

    if (cap.isOpened()== False):
        print("Error opening video file")

    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)
            if results.multi_hand_landmarks:
                for data_point in results.multi_hand_landmarks:
                    for point in handsModule.HandLandmark:
                        x_coord.append(data_point.landmark[point].x)
                        y_coord.append(data_point.landmark[point].y)
                        z_coord.append(data_point.landmark[point].z)

    cap.release()
    columns=[]
    for point in handsModule.HandLandmark:
    for c in ['x','y','z']:
        name='{}_{}'.format(point,c)
        columns.append(name)
    return x_coord, y_coord, z_coord, columns


