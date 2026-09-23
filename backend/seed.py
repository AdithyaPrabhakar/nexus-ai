from app.database import SessionLocal
from app.models.user import User
from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


db = SessionLocal()

try:
    existing_user = (
        db.query(User)
        .filter(User.email == "adi@nexusai.com")
        .first()
    )

    if existing_user:
        print("Test user already exists.")
    else:
        password_hash = pwd_context.hash("Password@123")

        user = User(
            name="Adithya",
            email="adi@nexusai.com",
            password_hash=password_hash,
            role="EMPLOYEE"
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        print(f"Test user created with ID: {user.id}")

finally:
    db.close()