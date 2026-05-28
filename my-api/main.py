from fastapi import FastAPI

app = FastAPI()

# Fake DB
books =[
    {"id":1, "title":"Harry Porter", "availability":True},
    {"id":2, "title":"Swift", "availability":False},
    {"id":3, "title":"Intentional Relationships", "availability":True},
]

# Home Route

@app.get("/")
def home():
    return {"message":"Ade library API"}
            
#Get all book

@app.get("/books")
def get_book():
    return books