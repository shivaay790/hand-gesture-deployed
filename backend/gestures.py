# gestures.py
import cv2
import mediapipe as mp
import config

class GestureRecognizer:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            max_num_hands=config.MAX_NUM_HANDS,
            min_detection_confidence=config.MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=config.MIN_TRACKING_CONFIDENCE
        )
        # Standard finger tip and knuckle indices
        self.tip_ids = [8, 12, 16, 20]

    def process_frame(self, frame):
        # Convert to RGB and process landmarks
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        
        gesture_id = 0
        landmarks_list = []
        
        if results.multi_hand_landmarks:
            # We track the first detected hand
            hand_landmarks = results.multi_hand_landmarks[0]
            self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
            
            # Save raw landmark coordinates
            for lm in hand_landmarks.landmark:
                landmarks_list.append(lm)
                
            opened_fingers = []
            
            # 1. Evaluate 4 Fingers (Index, Middle, Ring, Pinky)
            # Check if finger tip y-coordinate is above pip joint y-coordinate
            for tip in self.tip_ids:
                if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                    opened_fingers.append(1)
                else:
                    opened_fingers.append(0)
                    
            # 2. Evaluate Thumb
            # Checking horizontal placement relative to knuckle structure
            if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
                opened_fingers.insert(0, 1)
            else:
                opened_fingers.insert(0, 0)
                
            gesture_id = sum(opened_fingers)
            
        return gesture_id, landmarks_list, frame