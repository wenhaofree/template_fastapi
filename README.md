# Aistak_FastAPI 项目

这是一个基于FastAPI框架的Python Web应用项目。

## 项目结构

```
├── main.py              # 应用入口文件
├── requirements.txt     # 项目依赖
├── test_database.py     # 数据库连接测试脚本
├── app/                 # 应用核心代码
│   ├── core/           # 核心配置
│   │   ├── config.py   # 应用配置
│   │   └── database.py # 数据库配置
│   ├── models/         # 数据模型
│   │   └── user.py     # 用户模型
│   └── routers/        # 路由处理
│       ├── users.py    # 用户相关路由
│       └── health.py   # 健康检查路由
├── tests/              # 测试文件
│   ├── test_main.py    # 主要测试用例
│   └── test_database.py # 数据库测试用例
└── .env.example        # 环境变量示例
```

## 快速开始

### 使用 uv (推荐)

1. 安装依赖：
```bash
uv sync --extra dev
```

2. 复制环境变量文件：
```bash
cp .env.example .env
```

3. 配置数据库连接：
编辑 `.env` 文件，设置数据库连接信息：
```
DATABASE_URL=postgresql://username:password@host:port/database_name?sslmode=prefer
```

4. 测试数据库连接：
```bash
make test-db
# 或
uv run python test_database.py
```

5. 启动应用：
```bash
uv run uvicorn main:app --reload
```

或使用 Makefile：
```bash
make init  # 初始化项目
make run   # 启动开发服务器
```

### 使用传统方式

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 启动应用：
```bash
python main.py
```

## 访问API文档
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 开发命令

```bash
# 运行测试
uv run pytest tests/
# 或
make test

# 代码格式化
uv run ruff format .
# 或
make format

# 代码检查
uv run ruff check .
# 或
make lint

# 修复代码问题
make fix

# 测试数据库连接
make test-db

# 运行数据库相关测试
make test-db-unit
```

## API端点

### 基础端点
- `GET /` - 根路径

### 健康检查端点
- `GET /api/v1/health/` - 基本健康检查
- `GET /api/v1/health/database` - 数据库连接健康检查
- `GET /api/v1/health/database/info` - 获取数据库详细信息

### 用户管理端点
- `GET /api/v1/users/` - 获取所有用户
- `POST /api/v1/users/` - 创建新用户
- `GET /api/v1/users/{user_id}` - 获取指定用户

## 数据库配置

项目使用 PostgreSQL 数据库，配置信息在 `.env` 文件中：

```env
DATABASE_URL=postgresql://username:password@host:port/database_name?sslmode=prefer
```

### 数据库功能
- 自动连接池管理
- 连接健康检查
- 启动时自动测试连接
- 详细的错误日志记录

### 测试数据库连接
```bash
# 使用独立测试脚本
python test_database.py

# 使用 Makefile
make test-db

# 运行单元测试
make test-db-unit
```