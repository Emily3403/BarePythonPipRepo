from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from myproject.db.db_conf import DataBase
from sqlalchemy import Text, Enum as SQLEnum
from sqlalchemy.orm import mapped_column, Mapped, composite


class Color(Enum):
    red = 1
    green = 2
    blue = 3


@dataclass
class Measurement:
    name: str
    description: str

    time: datetime
    success: bool
    value: float


class SimpleModel(DataBase):  # type:ignore[valid-type, misc]
    __tablename__ = "simple_models"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    optional_author: Mapped[str | None] = mapped_column(Text, nullable=True)

    color: Mapped[Color] = mapped_column(SQLEnum(Color), nullable=False)
    measurement: Mapped[Measurement] = composite(
        mapped_column("measurement_name"), mapped_column("measurement_description"),
        mapped_column("measurement_time"), mapped_column("measurement_success"), mapped_column("measurement_value"),
    )
