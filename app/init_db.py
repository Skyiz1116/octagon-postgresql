from app.db.db import engine, Base, SessionLocal
from app.db import crud

Base.metadata.create_all(bind=engine)
db = SessionLocal()

cat1 = crud.create_category(db, "Фантастика")
cat2 = crud.create_category(db, "Детективы")

crud.create_book(db, "Дюна", "Научно-фантастический роман", 599.99, cat1.id)
crud.create_book(db, "Основание", "Классика научной фантастики", 499.99, cat1.id)
crud.create_book(db, "Марсианин", "Выживание на Марсе", 549.99, cat1.id)
crud.create_book(db, "Шерлок Холмс", "Приключения детектива", 399.99, cat2.id)
crud.create_book(db, "Преступление и наказание", "Психологический детектив", 449.99, cat2.id)

db.close()
print("База данных инициализирована!")