from fastapi import FastAPI
from api.user_api import router as user_router

app = FastAPI()
app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "Multi-layer architecture app"}