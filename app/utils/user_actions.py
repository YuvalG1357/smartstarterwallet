from sqlalchemy.exc import IntegrityError
from app.db.database import SessionLocal
from app.models.user import User

def create_user(username, password):
    session = SessionLocal()

    try:
        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit()
        print(" User created successfully")

    except IntegrityError:
        session.rollback()
        print("Username already exists")

    except Exception as e:
        session.rollback()
        print(f" An unexpected error occurred: {e}")

    finally:
        session.close()

def login_user(username, password):
    session = SessionLocal()

    try:
        user = session.query(User).filter_by(username=username).first()
        if user and user.password == password:
            print("Login successful")
            return user
        else:
            print("Invalid username or password")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        session.close()