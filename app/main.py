from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .models import LoanInput, AuditResult, SessionLocal, Loan, Base, engine
from agents.audit_workflow import app as agent_workflow
import os

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ARIA Agent Stack", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow Streamlit to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/audit")
def audit_loan(loan_data: LoanInput, db: Session = Depends(get_db)):
    # Run LangGraph agent workflow
    result = agent_workflow.invoke({"loan": loan_data.dict()})
    
    # Extract the result dictionary from the state
    r = result["result"]
    
    return {
        "corrected_net_rental": r["corrected_net"],
        "corrected_dti": r["corrected_dti"],
        "dti_variance": r["dti_variance"],
        "defect_code": r["defect_code"],
        "severity": r["severity"],
        "severity_desc": r["severity_desc"],
        "explanation": r["explanation"],
        "rule_references": ["Selling Guide B3-3.1-08: Rental Income", "Selling Guide B3-6-02: DTI"]
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
