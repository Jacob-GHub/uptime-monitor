from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, UniqueConstraint, CheckConstraint, Index
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True, nullable = False)
    email = Column(String, unique=True, index=True, nullable = False)
    hashed_password = Column(String, nullable = False)

class Website(Base):
    __tablename__ = "websites"

    __table_args__ = (
        UniqueConstraint("url", "user_id"),
        CheckConstraint("monitoring_interval > 0")
    )

    id = Column(Integer, primary_key=True)
    monitoring_interval = Column(Integer, nullable = False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    url = Column(String, nullable=False)
    

class MonitoringResult(Base):
    __tablename__ = "monitoring_results"
    __table_args__ = (
        Index("idx_website_time","website_id", "time_of_check"),
    )

    id = Column(Integer, primary_key=True)
    time_of_check = Column(DateTime(timezone=True),nullable=False)
    response_time = Column(Integer)
    updown_status = Column(Boolean, nullable = False)
    http_code = Column(Integer)
    website_id = Column(Integer, ForeignKey("websites.id"), nullable = False)



