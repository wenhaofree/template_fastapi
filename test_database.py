#!/usr/bin/env python3
"""
数据库连接测试脚本
用于测试数据库连接是否正常工作
"""

import sys
import os
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from app.core.database import test_database_connection, get_database_info
from app.core.config import settings

def main():
    """主测试函数"""
    print("=" * 60)
    print("🔍 数据库连接测试")
    print("=" * 60)
    
    # 显示配置信息
    print(f"📋 配置信息:")
    print(f"   项目名称: {settings.PROJECT_NAME}")
    print(f"   版本: {settings.VERSION}")
    print(f"   调试模式: {settings.DEBUG}")
    
    # 隐藏密码显示数据库URL
    masked_url = settings.DATABASE_URL
    if '@' in masked_url:
        parts = masked_url.split('@')
        credentials = parts[0].split('//')[-1]
        if ':' in credentials:
            user, password = credentials.split(':', 1)
            masked_url = masked_url.replace(f"{user}:{password}", f"{user}:***")
    
    print(f"   数据库URL: {masked_url}")
    print()
    
    # 测试数据库连接
    print("🔗 测试数据库连接...")
    is_connected, message = test_database_connection()
    
    if is_connected:
        print(f"✅ {message}")
        print()
        
        # 获取数据库详细信息
        print("📊 数据库信息:")
        db_info = get_database_info()
        
        if db_info.get("status") == "connected":
            print(f"   状态: {db_info['status']}")
            print(f"   数据库名: {db_info['database_name']}")
            print(f"   用户: {db_info['user']}")
            print(f"   版本: {db_info['version'][:50]}...")  # 截断长版本信息
        else:
            print(f"❌ 获取数据库信息失败: {db_info.get('error')}")
            
    else:
        print(f"❌ {message}")
        print()
        print("💡 可能的解决方案:")
        print("   1. 检查数据库服务是否运行")
        print("   2. 检查数据库连接参数是否正确")
        print("   3. 检查网络连接")
        print("   4. 检查数据库用户权限")
        return 1
    
    print()
    print("=" * 60)
    print("✨ 测试完成")
    print("=" * 60)
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n⚠️  测试被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 测试过程中发生错误: {e}")
        sys.exit(1)
