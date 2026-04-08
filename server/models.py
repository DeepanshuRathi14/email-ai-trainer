from pydantic import BaseModel

class Observation(BaseModel):
    email: str
    task: str
    step: int

class Action(BaseModel):
    response: str