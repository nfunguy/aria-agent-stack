from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import datetime
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./aria.db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Loan(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True, index=True)
    loan_number = Column(String, unique=True)
    borrower_income = Column(Float)
    total_obligations = Column(Float)
    gross_rent = Column(Float)
    pitia = Column(Float)
    lender_net_rental = Column(Float)
    submitted_dti = Column(Float)
    audit_status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

class LoanInput(BaseModel):
    loan_number: str
    borrower_income: float
    total_obligations: float
    gross_rent: float
    pitia: float
    lender_net_rental: float
    submitted_dti: float

class AuditResult(BaseModel):
    corrected_net_rental: float
    corrected_dti: float
    dti_variance: float
    defect_code: str
    severity: str
    rule_references: list[str]
