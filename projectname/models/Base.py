from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass


engine = create_engine("sqlite:///projectname/models/db/database.db")
