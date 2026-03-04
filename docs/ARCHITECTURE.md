# ARIA Technical Architecture

**Author**: Niloy Sengupta, VP Consult, US Financial Services, Kyndryl
**Version**: 1.0

## 1. System Overview
ARIA is a multi-agent AI system that automatically audits rental income calculations in mortgage loan files against Fannie Mae Selling Guide Section B3-3.1-08.

## 2. Architecture
It uses a containerized microservices architecture:
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **Agents**: LangGraph
- **Policy**: Open Policy Agent (OPA)
- **Database**: SQLite