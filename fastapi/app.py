import uuid

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# configuration
DEBUG = True

# instantiate the app
app = FastAPI()

# enable CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Book(BaseModel):
    id: str = None # needs to have default to allow creation without id (/books POST)
    title: str
    author: str
    read: bool = False


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


@app.get("/books")
def get_all_books():
    response_object = {'status': 'success'}
    response_object['books'] = BOOKS
    return response_object

@app.post("/books")
def post_all_books(book:Book):
    response_object = {'status': 'success'}
    BOOKS.append({
        'id': uuid.uuid4().hex,
        'title': book.title,
        'author': book.author,
        'read': book.read
    })
    response_object['message'] = 'Book added!'
    return response_object

def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

@app.put('/books/{book_id}')
def single_book(book:Book, book_id:str):
    response_object = {'status': 'success'}
    remove_book(book_id)
    BOOKS.append({
        'id': book_id,
        'title': book.title,
        'author': book.author,
        'read': book.read
    })
    response_object['message'] = 'Book updated!'
    return response_object

@app.delete('/books/{book_id}')
def single_book(book_id:str):
    response_object = {'status': 'success'}
    remove_book(book_id)
    response_object['message'] = 'Book removed!'
    return response_object

# sanity check route
@app.get("/ping")
def ping_pong():
    return 'pong!'


# if __name__ == '__main__':
#     app.run()
