from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Offer

engine = create_engine('sqlite:///nft.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

async def get_user_nfts(tg_id):
    session = Session()
    user = session.query(User).filter_by(tg_id=tg_id).first()
    if not user:
        return []
    
    # Здесь должна быть логика получения NFT из TON API
    return []  # Заглушка