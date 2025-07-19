from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging
from .config import settings

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 创建数据库引擎
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # 启用连接池预检查
    pool_recycle=300,    # 连接回收时间（秒）
    echo=settings.DEBUG  # 在调试模式下显示SQL语句
)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基础模型类
Base = declarative_base()

def get_db():
    """
    获取数据库会话的依赖函数
    用于FastAPI的依赖注入
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_database_connection():
    """
    测试数据库连接是否正常
    返回: (bool, str) - (连接状态, 消息)
    """
    try:
        # 尝试连接数据库并执行简单查询
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            result.fetchone()
            
        logger.info("数据库连接测试成功")
        return True, "数据库连接正常"
        
    except SQLAlchemyError as e:
        error_msg = f"数据库连接失败: {str(e)}"
        logger.error(error_msg)
        return False, error_msg
    except Exception as e:
        error_msg = f"未知错误: {str(e)}"
        logger.error(error_msg)
        return False, error_msg

def get_database_info():
    """
    获取数据库基本信息
    返回: dict - 数据库信息
    """
    try:
        with engine.connect() as connection:
            # 获取数据库版本
            version_result = connection.execute(text("SELECT version()"))
            version = version_result.fetchone()[0]
            
            # 获取当前数据库名
            db_name_result = connection.execute(text("SELECT current_database()"))
            db_name = db_name_result.fetchone()[0]
            
            # 获取当前用户
            user_result = connection.execute(text("SELECT current_user"))
            user = user_result.fetchone()[0]
            
            return {
                "status": "connected",
                "database_name": db_name,
                "user": user,
                "version": version,
                "url": settings.DATABASE_URL.replace(settings.DATABASE_URL.split('@')[0].split('//')[1], "***")  # 隐藏密码
            }
            
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }
