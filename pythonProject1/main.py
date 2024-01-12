import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import Publisher, Book, Shop, Stock, Sale

base_name = 'postgres'
password = 'postgres'
DB = 'test3'
# DSN = 'postgresql://postgres:postgres@localhost:5432/test1'
DSN = f'postgresql://{base_name}:{password}@localhost:5432/{DB}'
engine = sqlalchemy.create_engine(DSN)
# create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()
# p1 = Publisher(name='Пушкин А.С.')
# p2 = Publisher(name='Тургенев И.С.')
# p3 = Publisher(name='Ремарк Э.М.')
# p4 = Publisher(name='Карамзин Н.')
# p5 = Publisher(name='Набоков В.')
# session.add_all([p1, p2, p3, p4, p5])
# session.commit()
# b1 = Book(title='Евгений Онегин', id_publisher=1)
# b2 = Book(title='Капитанская дочка', id_publisher=1)
# b3 = Book(title='Ася', id_publisher=2)
# b4 = Book(title='Отцы и дети', id_publisher=2)
# b7 = Book(title='Три товарища', id_publisher=3)
# b5 = Book(title='Лолита', id_publisher=5)
# b6 = Book(title='Ночь в Лиссабоне', id_publisher=3)
# b8 = Book(title='Лиза', id_publisher=4)
# session.add_all([b1, b2])
# session.commit()
# s1 = Shop(name='Буквоед')
# s2 = Shop(name='Книжный дом')
# s3 = Shop(name='Читай город')
# session.add_all([s1, s2, s3])
# session.commit()
# st1 = Stock(id_book=1, id_shop=1, count=3)
# st2 = Stock(id_book=1, id_shop=2, count=1)
# st3 = Stock(id_book=2, id_shop=3, count=3)
# st4 = Stock(id_book=2, id_shop=2, count=3)
# st5 = Stock(id_book=4, id_shop=2, count=2)
# st6 = Stock(id_book=5, id_shop=1, count=3)
# st7 = Stock(id_book=5, id_shop=2, count=2)
# st8 = Stock(id_book=6, id_shop=3, count=4)
# st9 = Stock(id_book=7, id_shop=3, count=4)
# st10 = Stock(id_book=8, id_shop=1, count=4)
# session.add_all([st1, st2, st3,  st5, st6, st7, st8, st9, st10])
# session.commit()
# sal1 = Sale(price='1000', date_sale='2024-01-08', id_stock=10, count=8)
# sal2 = Sale(price='400', date_sale='2024-01-09', id_stock=11, count=2)
# sal3 = Sale(price='800', date_sale='2024-01-09', id_stock=12, count=3)
# sal4 = Sale(price='700', date_sale='2024-01-09', id_stock=13, count=2)
# sal5 = Sale(price='200', date_sale='2024-01-09', id_stock=14, count=4)
# sal6 = Sale(price='150', date_sale='2024-01-09', id_stock=15, count=4)
# sal7 = Sale(price='190', date_sale='2024-01-08', id_stock=16, count=7)
# sal8 = Sale(price='810', date_sale='2024-01-11', id_stock=17, count=2)
# sal9 = Sale(price='950', date_sale='2024-01-12', id_stock=18, count=4)
# session.add_all([sal2, sal3, sal4, sal6, sal5, sal6, sal7, sal8])
# session.commit()

print('Введите имя или идентификатор автора')
author = input()
if author.isnumeric():
    a = int(author)
    for c in session.query(Sale).join(Stock).join(Shop).join(Book).join(Publisher).filter(Publisher.id == a):
        print(c)
else:

    for c in session.query(Sale).join(Stock).join(Shop).join(Book).join(Publisher).filter(Publisher.name == author):
        print(c)
session.close()
