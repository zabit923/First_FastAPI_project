from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData




metadata = MetaData()

operation = Table(
    'operation',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('quantity', String),
    Column('figi', String),
    Column('instrument_type', String, nullable=False),
    Column('data', TIMESTAMP),
    Column('type', String),
)