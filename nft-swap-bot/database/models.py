from sqlalchemy import Column, Integer, String, JSON, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, unique=True)
    wallet_address = Column(String)

class Offer(Base):
    __tablename__ = 'offers'
    id = Column(Integer, primary_key=True)
    from_user = Column(Integer)
    to_user = Column(Integer)
    give_nft = Column(JSON)  # {name, collection, image_url}
    want_nft = Column(JSON)
    status = Column(String, default='pending')