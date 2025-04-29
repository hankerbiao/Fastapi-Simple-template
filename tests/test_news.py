from datetime import datetime

import pytest
from fastapi import status
from sqlmodel import Session, select

from models.news import NewNews


def test_create_news(client, db_session: Session):
    """测试创建新闻"""
    # 准备测试数据
    test_news = {
        "url": "https://test.com/news/1",
        "title": "测试新闻",
        "tags": "测试,标签",
        "summary": "这是一条测试新闻",
        "isFinanceOrEstate": True,
        "editor_time": datetime.utcnow().isoformat(),
    }
    
    # 如果API有创建接口，可以测试API
    # response = client.post("/api/v1/news", json=test_news)
    # assert response.status_code == status.HTTP_201_CREATED
    
    # 直接测试模型和数据库操作
    db_news = NewNews(**test_news)
    db_session.add(db_news)
    db_session.commit()
    
    # 验证结果
    db_news = db_session.exec(select(NewNews).where(NewNews.url == test_news["url"])).first()
    assert db_news is not None
    assert db_news.title == test_news["title"]
    assert db_news.isFinanceOrEstate == test_news["isFinanceOrEstate"]


def test_get_news_list(client, db_session: Session):
    """测试获取新闻列表"""
    # 准备测试数据
    test_news = {
        "url": "https://test.com/news/2",
        "title": "测试新闻2",
        "tags": "测试,标签",
        "summary": "这是一条测试新闻2",
        "isFinanceOrEstate": False,
        "editor_time": datetime.utcnow(),
    }
    db_news = NewNews(**test_news)
    db_session.add(db_news)
    db_session.commit()
    
    # 测试获取列表API
    response = client.get("/api/v1/news")
    assert response.status_code == status.HTTP_200_OK
    
    # 验证结果
    data = response.json()
    assert "items" in data
    assert data["total"] >= 1 