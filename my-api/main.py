from fastapi import FastAPI
from httpx import request


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
    return {"message":"Ade's library API"}
            
#Get all book

@app.get("/books")
def get_book():
    return books

@app.get('/books/available', methods=['GET']) 

def get_available_books():
    available_books = [book for book in books if book['available']] 
    return (available_books)

@app.get('/books/<int:book_id>/availability', methods=['GET']) 

def check_book_availability(book_id): 
    book = next((book for book in books if book['id'] == book_id), None) 
    
    if not book: return {
        
        "error": "Book not found"
        
        }, 404 
    
    return { 
        
        "id": book['id'], "title": book['title'], "available": book['available'] 
        
        }

@app.put('/books/<int:book_id>', methods=['PUT', 'PATCH']) 

def update_book(book_id): 
    
    book = next((book for book in books if book['id'] == book_id), None) 
    
    if not book: return {"error": "Book not found"
                         
                         }, 404 
    
    data = request.get_json() 
    
    if 'title' in data: book['title'] = data['title'] 
    
    return { 
        
        "message": "Book updated successfully", "book": book 
        
        }


@app.delete('/books/<int:book_id>', methods=['DELETE']) 

def delete_book(book_id): 
    
    global books 
    
    book = next((book for book in books if book['id'] == book_id), None) 
    
    if not book: 
        
        return {
            
            "error": "Book not found"
            
            }, 404 
    
    books = [b for b in books if b['id'] != book_id] 
    
    return { 
        
        "message": "Book deleted successfully" 
        
        }