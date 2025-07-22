from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# יצירת מנוע מסד נתונים
engine = create_engine("sqlite:///wallet.db", echo=True)

# יצירת session
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# בסיס למחלקות (User, Wallet וכו')
Base = declarative_base()

