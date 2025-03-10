from fastapi import FastAPI
from datetime import datetime
from models import TimeResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/time", response_model=TimeResponse)
async def get_time():
    return TimeResponse(
        current_time=datetime.now(),
        timezone=datetime.now().astimezone().tzname()
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
