import hashlib
import json
import logging
import random
import string
import time
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union

logger = logging.getLogger(__name__)


def generate_random_string(length: int = 8) -> str:
    """生成指定长度的随机字符串"""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def hash_password(password: str) -> str:
    """哈希密码"""
    return hashlib.sha256(password.encode()).hexdigest()


def calculate_time_difference(start_time: datetime, end_time: Optional[datetime] = None) -> timedelta:
    """计算时间差"""
    if end_time is None:
        end_time = datetime.utcnow()
    return end_time - start_time


def format_datetime(dt: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """格式化日期时间"""
    return dt.strftime(format_str)


def paginate(items: List[Any], page: int, page_size: int) -> Dict[str, Any]:
    """分页处理函数"""
    start = (page - 1) * page_size
    end = start + page_size
    
    return {
        "items": items[start:end],
        "total": len(items),
        "page": page,
        "page_size": page_size,
        "pages": (len(items) + page_size - 1) // page_size
    }


def safe_json_loads(json_str: str, default: Any = None) -> Any:
    """安全解析JSON字符串"""
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError) as e:
        logger.warning(f"JSON解析错误: {e}")
        return default


class Timer:
    """简单的计时器类，用于性能测量"""
    
    def __init__(self, name: str = ""):
        self.name = name
        self.start_time = 0
    
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.time() - self.start_time
        logger.info(f"计时器 {self.name}: {elapsed:.4f} 秒")
