# 🛡️ ARIA - Agentic Rental Income Auditor
**An open-source agentic AI system for automated mortgage compliance checking.**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge)](https://aria-agent-stack-demo.streamlit.app/)
[![Backend API](https://img.shields.io/badge/⚙️_Backend_API-Render-46E3B7?style=for-the-badge)](https://aria-agent-stack.onrender.com/docs)
[![GitHub](https://img.shields.io/badge/📂_Source_Code-GitHub-181717?style=for-the-badge&logo=github)](https://github.com/nfunguy/aria-agent-stack)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 What is ARIA?

ARIA is an open-source demo version of a **multi-agent AI system** that automatically audits rental income calculations in mortgage loan files against industry underwriting guidelines (such as Fannie Mae Selling Guide B3-3.1-08).

- **Policy as Code**: Open Policy Agent (OPA) enforces deterministic rules.
- **Agent Orchestration**: LangGraph workflows coordinate computational logic.
- **Explainable AI**: Chain of Thought reasoning with policy citations.
- **Containerized**: Fully deployable via Docker.
# 🛡️ ARIA - Agentic Rental Income Auditor

**Demo of agentic AI system for automated mortgage compliance checking, built for Fannie Mae loans by Niloy Sengupta, VP Consult, US Financial Services, Kyndryl.**

[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge)](https://aria-agent-stack-demo.streamlit.app/)
[![Backend API](https://img.shields.io/badge/⚙️_Backend_API-Render-46E3B7?style=for-the-badge)](https://aria-agent-stack.onrender.com/docs)
[![GitHub](https://img.shields.io/badge/📂_Source_Code-GitHub-181717?style=for-the-badge&logo=github)](https://github.com/nfunguy/aria-agent-stack)

---

## 🎯 What is ARIA?

ARIA is a **multi-agent AI system** that automatically audits rental income calculations in mortgage loan files against Fannie Mae Selling Guide policies. It demonstrates Kyndryl's Agentic AI Framework capabilities, highlighting Policy as Code:

- **Policy as Code**: Open Policy Agent (OPA) enforces Fannie Mae Selling Guide B3-3.1-08
- **Agent Orchestration**: LangGraph workflows coordinate deterministic + LLM-based agents
- **Human-in-the-Loop**: Explainable AI with Chain of Thought reasoning for compliance officers
- **Trustable AI**: Composite Trust Architecture with audit trails and rule citations

### The Problem
Rental income miscalculation has been the **#1 or #2 loan defect** at Fannie Mae for 8+ consecutive quarters. Manual QC review is slow, inconsistent, and error-prone.

### The Solution
ARIA automates 100% of rental income audits, detecting defects in milliseconds with full explainability and policy citations.

---

## 🚀 Quick Start

### Try the Live Demo (No Installation Required)
👉 **[Launch ARIA Dashboard](https://aria-agent-stack-demo.streamlit.app/)**

1. Select a scenario from the dropdown (Scenario B shows a Critical defect)
2. Click "Execute Agentic Audit"
3. Review the agent's Chain of Thought explanation

### Run Locally with Docker
```bash
# Clone the repository
git clone https://github.com/nfunguy/aria-agent-stack.git
cd aria-agent-stack

# Start all services
docker compose up --build

# Access the app
open http://localhost:8501

## 🤝 Contributing

We welcome contributions to ARIA! Since this is an open-source project, please feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

The MIT License is a permissive free software license that puts very few restrictions on reuse, meaning you can freely use, modify, and distribute this code for both commercial and non-commercial purposes.