from pydantic import BaseModel

class todo(BaseModel):
    title:str
    description:str