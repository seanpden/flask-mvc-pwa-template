from projectname.models.Base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Template(Base):
    __tablename__ = "template"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"Template(id=({self.id!r}, title={self.title!r}))"
