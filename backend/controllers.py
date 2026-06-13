# controllers.py
import pyautogui
import serial
import config

# Fail-safe protection: Moving mouse to upper-left corner aborts PyAutoGUI execution
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.01

class ActionController:
    def __init__(self):
        self.serial_conn = None
        if config.SERIAL_ENABLED:
            try:
                self.serial_conn = serial.Serial(config.SERIAL_PORT, config.BAUD_RATE, timeout=0.1)
                print(f"Serial port connected to {config.SERIAL_PORT}")
            except Exception as e:
                print(f"Serial connection failed: {e}. Defaulting to dummy stream.")

        # Actions map for HUD text display
        self.robot_actions = {0: "STOP", 1: "MOVE UP", 2: "MOVE DOWN", 3: "MOVE LEFT", 4: "MOVE RIGHT", 5: "FORWARD"}

    def execute(self, gesture_id, landmarks):
        profile = config.CURRENT_PROFILE
        
        # Stream over serial if hardware mode is active
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.write(f"{gesture_id}\n".encode())

        # EXECUTION PROFILE 1: Geometry Dash (Jump Only)
        if profile == "GEOMETRY_DASH":
            if gesture_id == 1:
                pyautogui.press('space')
                return "JUMP (SPACE)"
            return "IDLE"

        # EXECUTION PROFILE 2: Fruit Ninja (Cursor Tracking + Drag to Slice)
        elif profile == "FRUIT_NINJA":
            if len(landmarks) > 0:
                # Use index tip coordinates (Index 8)
                index_tip = landmarks[8]
                screen_w, screen_h = pyautogui.size()
                
                # Scale coordinates up to screen resolution matches
                target_x = int(index_tip.x * screen_w)
                target_y = int(index_tip.y * screen_h)
                
                if gesture_id == 2:  # Two fingers extended implies "Active Slice Mode"
                    pyautogui.dragTo(target_x, target_y, button='left')
                    return f"SLICING at ({target_x}, {target_y})"
                else:
                    pyautogui.moveTo(target_x, target_y)
                    return f"MOVING HOVER at ({target_x}, {target_y})"
            return "NO HAND DETECTED"

        # EXECUTION PROFILE 3: Autonomous Physical Robot Control Loop
        elif profile == "ROBOT":
            action = self.robot_actions.get(gesture_id, "STOP")
            return f"ROBOT ACTION -> {action}"
            
        return "UNKNOWN PROFILE"