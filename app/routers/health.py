from fastapi import APIRouter, HTTPException
from app.core.database import test_database_connection, get_database_info

router = APIRouter(prefix="/health", tags=["健康检查"])

@router.get("/")
async def health_check():
    """
    基本健康检查
    """
    return {
        "status": "healthy",
        "message": "服务运行正常"
    }

@router.get("/database")
async def database_health_check():
    """
    数据库连接健康检查
    """
    is_connected, message = test_database_connection()
    
    if not is_connected:
        raise HTTPException(status_code=503, detail=message)
    
    return {
        "status": "healthy",
        "message": message,
        "database_info": get_database_info()
    }

@router.get("/database/info")
async def get_db_info():
    """
    获取数据库详细信息
    """
    info = get_database_info()
    
    if info.get("status") == "error":
        raise HTTPException(status_code=503, detail=info.get("error"))
    
    return info
