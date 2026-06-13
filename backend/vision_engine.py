import cv2
import mediapipe as mp
import pyautogui
import webbrowser

class GestureEngine:
    def __init__(self):
        self.is_running = False
        self.cap = None
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.tip_ids = [8, 12, 16, 20]
        self.last_gesture = -1
        self.last_was_dragging = False
        # For smoothing mouse movement
        self.smooth_x = None
        self.smooth_y = None
        self.smoothing_factor = 0.5  # 0-1: higher = less smoothing

    def start(self, profile):
        self.is_running = True
        self.last_gesture = -1
        self.last_was_dragging = False
        self.smooth_x = None
        self.smooth_y = None
        
        # Open URLs based on profile
        if profile == "GEOMETRY_DASH":
            webbrowser.open("https://www.crazygames.com/game/geometry-dash-online")
        elif profile == "FRUIT_NINJA":
            webbrowser.open("https://poki.com/en/g/fruit-ninja")
        # ROBOT profile: no URL to open

        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        cv2.namedWindow('Gesture Cam', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('Gesture Cam', cv2.WND_PROP_TOPMOST, 1)
        cv2.resizeWindow('Gesture Cam', 320, 240)
        screen_width, _ = pyautogui.size()
        cv2.moveWindow('Gesture Cam', screen_width - 320 - 20, 20)

        hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )

        while self.is_running and self.cap.isOpened():
            success, frame = self.cap.read()
            if not success:
                continue

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)

            gesture_id = 0
            landmarks = []

            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                for lm in hand_landmarks.landmark:
                    landmarks.append(lm)

                opened_fingers = []
                for tip in self.tip_ids:
                    if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                        opened_fingers.append(1)
                    else:
                        opened_fingers.append(0)

                if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
                    opened_fingers.insert(0, 1)
                else:
                    opened_fingers.insert(0, 0)

                gesture_id = sum(opened_fingers)
                
                # Log gesture to terminal
                if gesture_id != self.last_gesture:
                    print(f"[GESTURE DETECTED] Finger count: {gesture_id}")
                    self.last_gesture = gesture_id

                self._execute_action(profile, gesture_id, landmarks)
            else:
                # No hand detected - release mouse button if pressed
                if self.last_was_dragging:
                    pyautogui.mouseUp(button='left')
                    self.last_was_dragging = False

            cv2.imshow('Gesture Cam', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.stop()

    def _execute_action(self, profile, gesture_id, landmarks):
        if profile == "GEOMETRY_DASH":
            # Closed fist (0 fingers) or 1 finger → jump continuously
            if gesture_id == 0 or gesture_id == 1:
                pyautogui.keyDown('space')
            else:
                pyautogui.keyUp('space')
        elif profile == "FRUIT_NINJA":
            if landmarks:
                index_tip = landmarks[8]
                screen_w, screen_h = pyautogui.size()
                target_x = int(index_tip.x * screen_w)
                target_y = int(index_tip.y * screen_h)
                
                # Smooth the movement
                if self.smooth_x is None or self.smooth_y is None:
                    self.smooth_x = target_x
                    self.smooth_y = target_y
                else:
                    self.smooth_x = self.smooth_x * self.smoothing_factor + target_x * (1 - self.smoothing_factor)
                    self.smooth_y = self.smooth_y * self.smoothing_factor + target_y * (1 - self.smoothing_factor)
                
                x = int(self.smooth_x)
                y = int(self.smooth_y)
                
                # Gesture: 1-2 fingers up → hold left click + move (slice)
                # Gesture: 0 fingers or 3+ fingers → just move (hover)
                is_dragging = 1 <= gesture_id <= 2
                
                if is_dragging:
                    if not self.last_was_dragging:
                        pyautogui.mouseDown(button='left')
                    pyautogui.moveTo(x, y)
                else:
                    if self.last_was_dragging:
                        pyautogui.mouseUp(button='left')
                    pyautogui.moveTo(x, y)
                
                self.last_was_dragging = is_dragging

    def stop(self):
        self.is_running = False
        # Release all keys/buttons
        pyautogui.keyUp('space')
        pyautogui.mouseUp(button='left')
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
