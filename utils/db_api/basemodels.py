from typing import List

from gino import Gino
import sqlalchemy
from gino.schema import GinoSchemaVisitor
from sqlalchemy import Column, DateTime

from data import config
from data.config import POSTGRES_URI

db = Gino()


# Пример из https://github.com/aiogram/bot/blob/master/app/models/db.py

class BaseModel(db.Model):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: sqlalchemy.Table = sqlalchemy.inspect(self.__class__)
        primary_key_columns: List[sqlalchemy.Column] = table.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimedBaseModel(BaseModel):
    __abstract__ = True

    created_at = Column(DateTime(True), server_default=db.func.now())
    updated_at = Column(DateTime(True),
                        default=db.func.now(),
                        onupdate=db.func.now(),
                        server_default=db.func.now())


async def create_db():
    await db.set_bind(POSTGRES_URI)
    db.gino: GinoSchemaVisitor
    await db.gino.create_all()
