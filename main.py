import requests
import json

def search_books(query):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()

        if result['totalItems'] > 0:
            books = result['items']

            for book in books:
                info = book['volumeInfo']
                print(f"Title: {info.get('title', 'N/A')}")
                print(f"Authors: {', '.join(info.get('authors', ['N/A']))}")
                print(f"Description: {info.get('description', 'N/A')}\n")
        else:
            print("No books found.")
    else:
        print("API request failed.")

book_title = 'python programming'  # replace with the book title or topic you want to search
search_books(book_title)
