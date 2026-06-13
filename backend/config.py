# config.py
import os

# Tracking Parameters
MIN_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE = 0.7
MAX_NUM_HANDS = 1

# Window Dimensions
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Control Profiles: "GEOMETRY_DASH", "FRUIT_NINJA", or "ROBOT"
CURRENT_PROFILE = "GEOMETRY_DASH" 

# Serial Configuration (Uncomment & change if deploying to hardware)
SERIAL_ENABLED = False
SERIAL_PORT = "COM3"  # '/dev/ttyUSB0' on Linux
BAUD_RATE = 9600

# CORS Configuration
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")