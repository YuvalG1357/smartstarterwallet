from app.db.database import Base, engine
from app.models.user import User

print("Initializing database...")
Base.metadata.create_all(bind=engine)
print("Tables created.")

