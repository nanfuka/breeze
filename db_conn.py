import psycopg2
import os
from pprint import pprint


class Database:
    def __init__(self):
        try:
            postgresdb = 'swett'
            Host="localhost"
            User="postgres"
            Password="test"

            if os.getenv('env') == "testing":
                postgresdb = 'fasters'
                Host="localhost"
                User="postgres"
                Password= "test"
            self.connection = psycopg2.connect(
                    database=postgresdb, host=Host, user=User,
                    password=Password, port="5432"
                )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint('cannot connect to database')

    def create_user_table(self):
        create_table = """CREATE TABLE IF NOT EXISTS user(
            userId SERIAL PRIMARY KEY,
            username VARCHAR UNIQUE,
            email VARCHAR,
            password VARCHAR)"""
        self.cursor.execute(create_table)
        self.connection.commit()

    # def create_menu_table(self):
    #     create_table = """CREATE TABLE IF NOT EXISTS menu(
    #         foodId SERIAL PRIMARY KEY,
    #         name VARCHAR,
    #         description VARCHAR,
    #         price BIGINT NOT NULL)"""
    #     self.cursor.execute(create_table)
    #     self.connection.commit()

    # def create_order_table(self):
    #     create_table = """CREATE TABLE IF NOT EXISTS orders(
    #         orderId SERIAL PRIMARY KEY,
    #         username VARCHAR NOT NULL,
    #         foodId INTEGER NOT NULL,
    #         status VARCHAR DEFAULT 'New',
    #         FOREIGN KEY (username)
    #             REFERENCES users (username)
    #             ON  DELETE CASCADE ON UPDATE CASCADE,
    #         FOREIGN KEY (foodId)
    #             REFERENCES menu (foodId)
    #             ON  DELETE CASCADE ON UPDATE CASCADE
    #     )"""
        # self.cursor.execute(create_table)
        # self.connection.commit()

database = Database()
database.create_user_table()
# database.create_menu_table()
# database.create_order_table()
