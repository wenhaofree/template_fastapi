.PHONY: install dev test run clean lint format

# 安装依赖
install:
	uv sync

# 安装开发依赖
dev:
	uv sync --extra dev

# 运行应用
run:
	uv run uvicorn main:app --reload

# 运行应用（生产模式）
start:
	uv run uvicorn main:app --host 0.0.0.0 --port 8000

# 运行测试
test:
	uv run pytest tests/ -v

# 运行测试并显示覆盖率
test-cov:
	uv run pytest tests/ -v --cov=app --cov-report=html

# 测试数据库连接
test-db:
	uv run python test_database.py

# 运行数据库相关测试
test-db-unit:
	uv run pytest tests/test_database.py -v

# 代码格式化
format:
	uv run ruff format .

# 代码检查
lint:
	uv run ruff check .

# 修复代码问题
fix:
	uv run ruff check . --fix

# 清理缓存
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage

# 初始化项目
init:
	uv sync --extra dev
	cp .env.example .env