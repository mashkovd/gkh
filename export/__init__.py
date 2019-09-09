from models import engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

