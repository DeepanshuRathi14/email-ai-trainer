from fastapi import FastAPI
from server.environment import EmailEnv
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # hackathon ke liye ok
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

env = EmailEnv()

class ResponseModel(BaseModel):
    response: str


@app.post("/reset")
def reset():
    return env.reset()


@app.post("/step")
def step(data: ResponseModel):
    return env.step(data.response)