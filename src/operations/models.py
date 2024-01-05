from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData
from sqlalchemy.sql import func




metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("quantity", String),
    Column("figi", String),
    Column("instrument_type", String, nullable=True),
    Column("date", TIMESTAMP(timezone=True), server_default=func.now()),
    Column("type", String),
)
