from model import todo


#mogoDB driver
import motor.motor_asyncio
print('hahaha')

try:
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
    print("haboub")

    # Your MongoDB operations here
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")


#creation database
# database=client.TodoList




#creation collection
# collection = database.todo
if client:
    
    print('hab')
    database = client['TodoList']  # Specify the name of the new database
    collection = database['todo']
 

async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    return document



async def fetch_all_todo():
    todos= []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(todo(**document))
    return todos




async def create_todo(todo):
    document= todo.dict()

    resulat = await collection.insert_one(document)
    return resulat


async def update_todo(title,description):
    await collection.update_one({"title":title},{"$set": {
        "description":description
    }})
    document = await collection.find_one({"title":title})
    return True


async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True








