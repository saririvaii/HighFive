"""
Hand detection Module
Handles MediaPipe hand detection and drawing
"""

import cv2
import mediapipe as mp
import numpy as np

class HandDetector:

    def __init__(self, max_hands=2, detection_conf=0.7, tracking_conf=0.5):
        """Initialise the hand detector"""

        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils

        self.hands = self.mp_hands.Hands(
            static_image_mode = False,
            max_num_hands = max_hands,
            min_detection_confidence = detection_conf,
            min_tracking_confidence = tracking_conf
        )

        # drawing specs for the red skeleton
        self.landmark_spec = mp.solutions.drawing_utils.DrawingSpec(
            color=(0,0,255), thickness=2, circle_radius = 2
        )
        self.connection_spec = mp.solutions.drawing_utils.DrawingSpec(
            color=(0,0,255), thickness=2
        )

    def detect_hands(self, frame):
        """detect hands in the frame and return results"""
        
        # covert bgr from cam to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #process the frame
        results =self.hands.process(rgb_frame)
        return results


    def draw_hands(self, frame, results):
        """Draw hand landmarks and connections on the frame"""

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:

                #draw the red lines
                self.mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.landmark_spec,
                    self.connection_spec
                )
        return frame

    def get_hand_count(self, results):
        """get the number of hands detected"""
        if results.multi_hand_landmarks:
            return len(results.multi_hand_landmarks)
        return 0

