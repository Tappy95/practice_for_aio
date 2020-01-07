from sqlalchemy import Table, Column, PrimaryKeyConstraint, Integer, String, TIMESTAMP,\
    Boolean, TEXT, DECIMAL
from sqlalchemy.dialects.mssql import TINYINT

from models import metadata


amazon_keyword_rank = Table(
    'amazon_keyword_rank', metadata,
    Column('asin', String),
    Column('keyword', String),
    Column('site', String),
    Column('rank', Integer),
    Column('aid', String),
    Column('update_time', TIMESTAMP),
    PrimaryKeyConstraint('asin', 'keyword', 'site', name='pk')
)

ebay_analysis_user = Table(
    'ebay_analysis_user', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('phone', Integer, ),
    Column('password', String(32)),
    Column('create_at', TIMESTAMP),
    Column('update_at', TIMESTAMP),
    PrimaryKeyConstraint('id', name='pk')
)

