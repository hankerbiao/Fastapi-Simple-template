from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Base(SQLModel):
    """基础模型类，包含通用字段"""

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)