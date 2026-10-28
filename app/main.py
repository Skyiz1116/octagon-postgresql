from app.db.db import SessionLocal
from app.db import crud

db = SessionLocal()

print("=== Категории ===")
for cat in crud.get_categories(db):
    print(f"ID: {cat.id}, Название: {cat.title}")

print("\n=== Книги ===")
for book in crud.get_books(db):
    cat = crud.get_category(db, book.category_id)
    print(f"ID: {book.id}, Название: {book.title}, Цена: {book.price}, Категория: {cat.title}")

db.close()