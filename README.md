# FastAPI项目模板

## 项目简介

这是一个基于FastAPI + Pydantic + SQLModel的快速开发模板，旨在帮助开发者快速搭建高性能的RESTful API服务。

## 技术栈

- **FastAPI**: 高性能异步API框架
- **Pydantic**: 数据验证和设置管理
- **SQLModel**: 结合了SQLAlchemy和Pydantic的ORM库
- **Uvicorn**: ASGI服务器
- **Alembic**: 数据库迁移工具
- **Python-dotenv**: 环境变量管理
- **Pytest**: 测试框架

## 项目结构

```
.
├── app/                    # 应用主目录
│   ├── __init__.py         # 应用初始化
│   ├── api/                # API相关代码
│   │   ├── __init__.py     # API路由注册
│   │   ├── deps.py         # 依赖注入
│   │   └── routes/         # 路由定义
│   └── middleware/         # 中间件
│       ├── __init__.py
│       └── error_handler.py # 错误处理中间件
├── models/                 # 数据模型目录
│   ├── __init__.py         # 模型导出
│   ├── base.py             # 基础模型类
│   └── news.py             # 新闻模型
├── migrations/             # 数据库迁移
│   ├── env.py              # 迁移环境配置
│   ├── script.py.mako      # 迁移脚本模板
│   └── versions/           # 迁移版本
├── tests/                  # 测试目录
│   ├── __init__.py
│   ├── conftest.py         # 测试配置
│   └── test_news.py        # 示例测试
├── utils/                  # 工具函数
│   ├── __init__.py
│   └── utils.py            # 通用工具
├── config.py               # 应用配置
├── main.py                 # 应用入口
├── pyproject.toml          # 项目依赖
├── alembic.ini             # Alembic配置
├── .env.example            # 环境变量示例
└── README.md               # 项目说明
```

## 功能特点

- 基于FastAPI的现代化API框架
- 采用SQLModel进行数据库建模和操作
- 完整的路由组织结构
- 内置CORS支持
- 统一的异常处理中间件
- 支持依赖注入
- 自动生成API文档
- 环境变量配置系统
- 数据库迁移支持
- 完整的测试框架
- 实用工具函数集

## 快速开始

### 环境要求

- Python 3.12+

### 安装

```bash
# 克隆仓库
git clone [https://github.com/yourusername/fastapi-template.git](https://github.com/hankerbiao/Fastapi-Simple-template.git)
cd fastapi-template

# 创建并激活虚拟环境
python -m venv venv
source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate

# 安装依赖
pip install -e .
```

### 配置

1. 复制环境变量示例文件
```bash
cp .env.example .env
```

2. 编辑.env文件，根据需要修改配置

### 数据库迁移

```bash
# 初始化数据库
alembic upgrade head

# 创建新的迁移（当模型变更时）
alembic revision --autogenerate -m "你的迁移说明"
```

### 运行

```bash
# 启动开发服务器
python main.py
```

访问 http://localhost:8001/docs 查看API文档。

### 测试

```bash
# 运行测试
pytest
```

## 项目配置

配置通过环境变量和config.py文件进行管理：

- **DATABASE_URL**: 数据库连接URL
- **APP_ENV**: 应用环境（development、production）
- **DEBUG**: 是否开启调试模式
- **SECRET_KEY**: 应用密钥
- **HOST**: 服务监听地址
- **PORT**: 服务监听端口

## 数据库模型

在models目录中定义数据模型：

```python
from datetime import datetime
from typing import Optional
from sqlmodel import Field
from models.base import Base

class Item(Base, table=True):
    __tablename__ = "items"
    
    name: str
    description: Optional[str] = None
    price: float
    is_active: bool = True
```

## 创建新路由

1. 在`app/api/routes/`目录下创建新的路由文件
2. 在`app/api/__init__.py`中注册路由

示例:

```python
# app/api/routes/items.py
from fastapi import APIRouter, HTTPException
from app.api.deps import SessionDep
from models import Item

router = APIRouter()

@router.get("/items")
async def get_items(db: SessionDep):
    items = db.exec(select(Item)).all()
    return {"items": items}
```

```python
# app/api/__init__.py
from fastapi import APIRouter
from app.api.routes import news, items

api_route = APIRouter()
api_route.include_router(news.router, tags=["新闻"])
api_route.include_router(items.router, tags=["商品"])
```

## 错误处理

项目使用统一的错误处理中间件，位于`app/middleware/error_handler.py`，可以根据需要添加自定义异常处理。

## 贡献指南

欢迎贡献代码或提出问题！请遵循以下步骤：

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

## 许可证

MIT
