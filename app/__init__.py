from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api import api_route
from app.middleware import ErrorHandlerMiddleware
from config import settings


def create_app() -> FastAPI:
    """创建FastAPI应用"""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
    )

    # 添加CORS中间件
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 在生产环境中应该更具体
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 添加错误处理中间件
    app.add_middleware(ErrorHandlerMiddleware)

    # 注册路由
    app.include_router(api_route, prefix=settings.API_PREFIX)

    @app.get("/")
    async def root():
        return {"message": "欢迎使用FastAPI模板"}

    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app
