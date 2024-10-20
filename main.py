from routes.routes import router
from startup.startup_tasks import on_startup

from fastapi import FastAPI

app = FastAPI()

# Register routes
app.include_router(router)

# Run startup tasks
@app.on_event("startup")
async def startup_event():
    await on_startup()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
