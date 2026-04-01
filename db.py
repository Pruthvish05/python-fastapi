from collections.abc import AsyncGenerator
from sqlalchemy import Text, create_engine, column, String,DateTime,ForeignKey
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
import datetime
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

class Posts(DeclarativeBase):
    __tablename__ = "posts"
    id = column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    caption = column(Text)
    url = column(String, nullable=False)
    created_at = column(DateTime, default=datetime.utcnow)
    file_name = column(String, nullable=False)
    file_type = column(String, nullable=False)

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)
async def create_db_with_tables() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(DeclarativeBase.metadata.create_all)
