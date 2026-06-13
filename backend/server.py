from fastapi import FastAPI
from pydantic import BaseModel
from vision_engine import GestureEngine
import threading
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

gesture_engine = GestureEngine()
engine_thread = None

class StartRequest(BaseModel):
    profile: str

@app.post("/api/start")
async def start_engine(request: StartRequest):
    global engine_thread
    if gesture_engine.is_running:
        return {"status": "already_running", "message": "System is already active"}
    
    engine_thread = threading.Thread(
        target=gesture_engine.start,
        args=(request.profile,),
        daemon=True
    )
    engine_thread.start()
    return {"status": "success", "message": f"System started in {request.profile} mode"}

@app.post("/api/stop")
async def stop_engine():
    gesture_engine.stop()
    return {"status": "success", "message": "System stopped successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2000)
