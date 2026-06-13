# main.py
import cv2
import config
from gestures import GestureRecognizer
from controllers import ActionController

def main():
    # Initialize capturing device
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.FRAME_HEIGHT)
    
    recognizer = GestureRecognizer()
    controller = ActionController()
    
    print(f"=== Framework Running ===")
    print(f"Active App Target Profile: {config.CURRENT_PROFILE}")
    print("Keep focus on the terminal window or move mouse to absolute top-left corner to crash-kill loop safely.")

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame processing frame instance.")
            continue

        # Flip horizontally for natural real-time mirror symmetry
        frame = cv2.flip(frame, 1)

        # Process landmarks and acquire current dynamic ID configuration
        gesture_id, landmarks, frame = recognizer.process_frame(frame)
        
        # Execute peripheral event maps matching target settings profile
        status_text = controller.execute(gesture_id, landmarks)

        # UI Visual HUD Render Block
        cv2.rectangle(frame, (12, 12), (380, 115), (20, 20, 20), -1) # Dark Translucent Box
        cv2.putText(frame, f"PROFILE: {config.CURRENT_PROFILE}", (22, 38), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 165, 255), 2)
        cv2.putText(frame, f"G-ID COUNT: {gesture_id}", (22, 68), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f"CMD: {status_text}", (22, 98), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        # Show frame output
        cv2.imshow("Hand Gesture Core Framework Integration UI", frame)

        # Quit execution check loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()