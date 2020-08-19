import asyncio

import asyncpg
from data import config


class Database:

    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                password=config.PGPASSWORD,
                host=config.ip
            )
        )

    async def create_table_users(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Users(
            id INT NOT NULL,
            Name VARCHAR(255) NOT NULL,
            email VARCHAR(255),
            phone_number VARCHAR(255),
            date_of_birth varchar(255),
            PRIMARY KEY (id))
            """
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = {num}" for num, item in enumerate(parameters, start=1)
        ])
        return sql, tuple(parameters)

    async def add_user(self, id: int, Name: str = None, email: str = None, phone_number: str = None,
                       date_of_birth: str = None):
        sql = " INSERT INTO Users(id,Name,email,phone_number, date_of_birth) VALUES($1,$2,$3,$4,$5)"
        await self.pool.execute(sql, id, Name, email, phone_number, date_of_birth)

    async def add_email(self, email, id):
        sql = " UPDATE Users SET  email = $1 WHERE id=$2"
        return await self.pool.execute(sql, email, id)

    async def add_phone(self, phone_number, id):
        sql = " UPDATE Users SET  phone_number = $1 WHERE id=$2"
        return await self.pool.execute(sql, phone_number, id)

    async def add_date(self, date_of_birth, id):
        sql = " UPDATE Users SET  date_of_birth = $1 WHERE id=$2"
        return await self.pool.execute(sql, date_of_birth, id)

    async def select_all_users(self, **kwargs):
        sql = "SELECT * FROM Users "
        return await self.pool.fetch(sql)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.pool.fetchrow(sql, *parameters)

    async def delete_users(self):
        sql = "DELETE FROM Users"
        await self.pool.execute(sql)
