from typing import Annotated, Generator

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import Session, SQLModel

from config import settings

# 创建数据库引擎
engine = create_engine(settings.DATABASE_URL)

# 创建所有表
SQLModel.metadata.create_all(engine)


def get_db() -> Generator[Session, None, None]:
    """获取数据库会话"""
    with Session(engine) as session:
        yield session


# 依赖注入类型
SessionDep = Annotated[Session, Depends(get_db)] 