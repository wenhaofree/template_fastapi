from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

# 模拟数据库
fake_users_db = []

@router.get("/", response_model=List[UserResponse])
async def get_users():
    return fake_users_db

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    user_dict = user.model_dump()
    user_dict["id"] = len(fake_users_db) + 1
    user_dict["is_active"] = True
    # 移除密码字段，实际项目中应该加密存储
    del user_dict["password"]
    
    fake_users_db.append(user_dict)
    return user_dict

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    for user in fake_users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="用户未找到")