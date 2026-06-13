# Hand Gesture Control System

A complete end-to-end hand gesture recognition and control system with web interface, built-in games, and robot/serial support.

## Features

- **Real-time hand gesture recognition** using MediaPipe
- **Multiple control modes**:
  - Geometry Dash (Jump Only - Space key)
  - Fruit Ninja (Mouse control + drag to slice)
  - Robot Control (Serial output for hardware)
  - Geometry Dash Demo (built-in mini game)
- **Visualizations**: Shows finger count and direction indicators
- **Live camera feed** in the web interface
- **FastAPI backend** with WebSocket communication
- **Modern responsive web frontend**

## Setup Instructions

### 1. Create Virtual Environment (Optional but Recommended)

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate
```

### 2. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 3. Run the Server

```powershell
python server.py
```

### 4. Open Browser

Navigate to `http://localhost:8000`

## Usage

1. Allow camera access when prompted
2. Select your desired mode from the dropdown
3. Use your hand gestures to control!

### Gesture Guide

- 0 fingers: Stop/Idle
- 1 finger: Jump/Up
- 2 fingers: Down
- 3 fingers: Left
- 4 fingers: Right
- 5 fingers: Forward

## Project Structure

```
├── backend/
│   ├── server.py          # FastAPI server with WebSocket
│   ├── main.py            # Original OpenCV-only mode
│   ├── gestures.py        # Gesture recognition logic
│   ├── controllers.py     # Action execution (pyautogui/serial)
│   ├── config.py          # Configuration settings
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
└── README.md
```

## Production Deployment

For production deployment:
- Use a process manager like `gunicorn` or `systemd`
- Consider using a reverse proxy like Nginx
- For minimal venv size, use `pip install --no-cache-dir`
- Optional: Remove unused dependencies (pyserial if no hardware)
