# from sqlalchemy import create_engine, Column, Integer, String, Boolean
# from sqlalchemy.orm import sessionmaker, declarative_base
#
# db_url = 'postgresql+psycopg2://postgres:22@localhost:5432/work_db'
#
# engine = create_engine(url=db_url)
# Session = sessionmaker(bind=engine)
# session = Session()
#
# Base = declarative_base()
#
#
# class Work(Base):
#
#     __tablename__ = 'work'
#
#     id = Column(Integer, autoincrement=True, primary_key=True)
#     name = Column(String(length=150))
#     age = Column(Integer)
#     phone_number = Column(String(length=150))
#     address = Column(String(length=150))
#     job = Column(String(length=150))
#     # is_active = Column(Boolean, default=False)
#
#     def add_user(self, name, age, phone_number, address, job):
#         user = session.add(Work(name=name, age=age, phone_number=phone_number, address=address,job=job))
#         session.commit()
#         return user
#
#     def delete_user(self, user_id):
#         user = session.query(Work).get(user_id)
#         session.commit()
#         return session.delete(user)
#
#     def get_user(self, user_id):
#         user = session.query(Work).get(user_id)
#         return user
#
#     def all_user(self):
#         users = session.query(Work).all()
#         return users
#
# # Base.metadata.create_all(engine)
#

import sqlite3


class Work:
    def __init__(self):
        self.connection = sqlite3.connect("work")
        self.cursor = self.connection.cursor()
        self.create_user()

    def create_user(self):
        self.cursor.execute("""
        create table if not exists user(
                id integer primary key,
                name varchar ,
                age integer ,
                phone_number varchar ,
                address varchar,
                job varchar
                )
        """)
        self.connection.commit()

    def add_user(self, name, age, phone_number, address,job):
        self.cursor.execute("""
            insert into user (name, age, phone_number, address,job) values (?, ?, ?, ?,?)
        """, (name, age, phone_number, address,job))
        self.connection.commit()

    def all_user(self):
        self.cursor.execute(f"""
            SELECT * from user
        """)
        return self.cursor.fetchall()


    def get_user(self, id):
        self.cursor.execute("""
            select * from user where id=?
        """, (id,))
        return self.cursor.fetchone()

    def delete_user(self, id):
        self.cursor.execute("""
            delete from user where id=?
        """, (id,))
        self.connection.commit()














