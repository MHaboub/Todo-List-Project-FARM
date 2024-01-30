from fastapi import FastAPI,HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from model import todo


#App object
app= FastAPI()



#origins= ['http://localhost,http://localhost:3000/,http://127.0.0.1:3000/']

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=['*']
)

from databse import (
    fetch_one_todo,
    fetch_all_todo,create_todo,
    update_todo,
    remove_todo
)

@app.get('/')
def read_root():
    return{"ping":"pong"}


@app.get("/api/todo/")
async def get_todo_by_id():
    response =await fetch_all_todo()
    return response


@app.get("/api/todo/{title}",response_model=todo)
async def get_todo(title):
    response = await fetch_one_todo(title)
    if response : 
        return response
    raise HTTPException(404,f"there is no TODO item with this title{title}")

@app.options("/api/todo/")
async def options_handler(request: Request, response: Response, path: str):
    # Set the appropriate CORS headers for the OPTIONS request
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response


@app.post("/api/todo",response_model=todo)
async def post_todo(todo:todo):
    document = todo
    result = await create_todo(document)
    if result.acknowledged:
        # If the insert operation is successful, return the created todo
        print('sa7a')
        return todo
    else:
        # If the insert operation fails, raise an exception or handle accordingly
        raise HTTPException(500, "Failed to create todo item")



@app.put("/api/todo/{title}")
async def put_todo(title:str,desc:str):
    response = await update_todo(title,desc)
    if response : 
        return response
    raise HTTPException(404,f"there is no TODO item with this title{title}")



@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response : 
        return "successfully deleted"+title
    raise HTTPException(404,f"there is no TODO item with this title{title}")


