from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routers import users, health
from app.core.config import settings
from app.core.database import test_database_connection
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    # 启动时的处理
    logger.info("应用启动中...")

    # 测试数据库连接
    is_connected, message = test_database_connection()
    if is_connected:
        logger.info(f"✅ {message}")
    else:
        logger.error(f"❌ {message}")
        logger.warning("应用将继续启动，但数据库功能可能不可用")

    yield

    # 关闭时的处理
    logger.info("应用正在关闭...")

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="FastAPI项目",
    lifespan=lifespan
)

# 包含路由
app.include_router(users.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "欢迎使用FastAPI!"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)