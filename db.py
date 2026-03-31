from collections.abc import AsyncGenerator
from sqlalchemy import text, create_engine, column, String,DateTime,ForeignKey
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
DATABASE_URL = "sqlite_+aiosqlite:///./test.db"