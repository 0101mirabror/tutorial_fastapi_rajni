from fastapi import FastAPI, Query, Path, Form, File, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
app = FastAPI()

'''Upload file using fast api and save it into folder'''
# define the folder path where the uploaded files will be saved
UPLOADS_FOLDER = "uploads"

# Create uploads folder if it doesn't exists
os.makedirs(UPLOADS_FOLDER, exist_ok=True)


# Route handler for handling POST requests to /uploads_file/
@app.post("/uploads_file/")
async def upload_file(file: UploadFile = File(...)):
    # Access the uploaded file using the UploadFile parameter
    # You can then use the file as needed, such as saving it, processing it ,etc.
    file_path = os.path.join(UPLOADS_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    # return a response indicating success and file details.
    return JSONResponse(content={"message": "File uploaded successfully", "filename": file.filename, 
    "content_type": file.content_type})

'''Accessing Form data'''
# @app.post("/submit_form/")
# async def submit_form(username: str = Form(...), password: str = Form(...)):
#     print("Username", username)
#     print("Password", password)
#     return {'message': 'form submitted successfully', 'username': username}


'''Pydantic schemas and Data Validation'''
# class  Item(BaseModel):
#     name: str
#     description: str = None
#     price: float
#     tax: float = None

# @app.post("/items/")
# async def create_item(item: Item):
#     print("Validated data", item.model_dump())
#     return {"message": "Item created successfully", 'data': item.model_dump()}

'''Parameter Validation'''
# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: bool = None

# Simple type validation
# l = []
# @app.post("/items/")
# async def create_item(item: Item):
#     # l.append(item)
#     return item

# # Query parameter validation
# @app.get("/items/")
# async def read_items(q: str = Query(None, min_length=3, max_length=50)):
#     return{'q': q}

# Path parameter validation
# @app.get("/items/{item_id}")
# async def read_item(item_id:int = Path(..., title='the ID of the item to get', ge=3)):
#     return {'item_id': item_id}
    

'''Path and Query parameters'''
#Path parameters
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}
# # http://localhost:8000/items/1

# #Query parameters
# @app.get("/items/")
# async def  read_item(item_id: int, q: str=None):
#     return {"item_id": item_id, "q": q}
# # http://localhost:8000/items/?item_id=6&q=test1

# # path and query parameters together
# @app.get("/items/{item_id}/")
# async def read_item(item_id: int, q:str = None):
#     return {"item_id": item_id, "q": q}
# #http://localhost:8000/items/4/?item_id=6&q=test1 


'''swagger integration with fastapi'''
# disable syntax highlighting
# app = FastAPI(swagger_ui_parameters={'syntaxHighlight': False})

# change the theme
# app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})


'''Hello world project'''
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
