import logging
from typing import Callable

from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from starlette.middleware.base import BaseHTTPMiddleware


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    """统一异常处理中间件"""

    def __init__(self, app: FastAPI):
        super().__init__(app)
        self.logger = logging.getLogger(__name__)

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        try:
            return await call_next(request)
        except SQLAlchemyError as e:
            self.logger.error(f"数据库错误: {str(e)}")
            return JSONResponse(
                status_code=500,
                content={"detail": "数据库错误", "message": str(e)},
            )
        except ValueError as e:
            self.logger.error(f"参数错误: {str(e)}")
            return JSONResponse(
                status_code=400,
                content={"detail": "参数错误", "message": str(e)},
            )
        except Exception as e:
            self.logger.error(f"服务器内部错误: {str(e)}")
            return JSONResponse(
                status_code=500,
                content={"detail": "服务器内部错误", "message": str(e)},
            ) 