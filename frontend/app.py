import streamlit as st
import requests
import os

API_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="Kyndryl ARIA", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for better styling
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .critical { border-left: 5px solid #ff4b4b; }
    .high { border-left: 5px solid #ff9f36; }
    .medium { border-left: 5px solid #ffe119; }
    .pass { border-left: 5px solid #00c04b; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ARIA by Kyndryl")
st.subheader("Agentic Rental Income Auditor for Fannie Mae Loans")
st.markdown("Automated compliance checking using Policy as Code and multi-agent workflow orchestration.")

# --- SCENARIO DATA DEFINITIONS ---
scenarios = {
    "Custom / Manual Entry": {
        "income": 8000.0, "debt": 3000.0, "rent": 1200.0, "piti": 1800.0, "lender_net": -200.0, "dti": 44.8
    },
    "Scenario A: Clean Loan (Pass)": {
        "income": 10000.0, "debt": 3000.0, "rent": 2000.0, "piti": 1500.0, "lender_net": 0.0, "dti": 30.0
    },
    "Scenario B: Rental Loss Understatement (Critical)": {
        "income": 8000.0, "debt": 3580.0, "rent": 1200.0, "piti": 1800.0, "lender_net": -200.0, "dti": 44.8
    },
    "Scenario C: ADU Over-Inclusion (High)": {
        "income": 6000.0, "debt": 2500.0, "rent": 2000.0, "piti": 800.0, "lender_net": 1200.0, "dti": 41.6
    }
}

# --- SIDEBAR UI ---
with st.sidebar:
    st.header("🧪 Select Demo Scenario")
    selected_scenario = st.selectbox(
        "Choose a test case to auto-fill data:",
        options=list(scenarios.keys())
    )
    
    # Get the data for the selected scenario
    s_data = scenarios[selected_scenario]
    
    st.divider()
    st.header("📋 Loan Data Input")
    loan_number = st.text_input("Loan Number", value="FNMA-987654")
    
    st.markdown("**Borrower Financials**")
    borrower_income = st.number_input("Borrower Base Income ($/mo)", value=s_data["income"], step=100.0)
    total_obligations = st.number_input("Total Debt Obligations ($/mo)", value=s_data["debt"], step=100.0)
    submitted_dti = st.number_input("Lender Submitted DTI (%)", value=s_data["dti"], step=0.1)
    
    st.markdown("**Subject Rental Property**")
    gross_rent = st.number_input("Gross Rent ($/mo)", value=s_data["rent"], step=100.0)
    pitia = st.number_input("Property PITI/A ($/mo)", value=s_data["piti"], step=100.0)
    lender_net = st.number_input("Lender Net Rental Income/Loss ($/mo)", value=s_data["lender_net"], step=100.0)

    run_btn = st.button("🚀 Execute Agentic Audit", type="primary", use_container_width=True)

# --- MAIN DASHBOARD AREA ---
if run_btn:
    with st.spinner("🤖 ARIA Agents analyzing loan against Selling Guide B3-3.1-08..."):
        response = requests.post(f"{API_URL}/audit", json={
            "loan_number": loan_number,
            "borrower_income": borrower_income,
            "total_obligations": total_obligations,
            "gross_rent": gross_rent,
            "pitia": pitia,
            "lender_net_rental": lender_net,
            "submitted_dti": submitted_dti
        })
        
        if response.status_code == 200:
            result = response.json()
            
            # Determine color based on severity
            sev_color = "pass"
            if result['severity'] == "Critical": sev_color = "critical"
            elif result['severity'] == "High": sev_color = "high"
            elif result['severity'] == "Medium": sev_color = "medium"
            
            # --- TOP ROW: Key Metrics ---
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.markdown(f"""
                <div class="metric-card {sev_color}">
                    <h4>Defect Code</h4>
                    <h2>{result['defect_code']}</h2>
                </div>
                """, unsafe_allow_html=True)
            with col2:
                st.markdown(f"""
                <div class="metric-card {sev_color}">
                    <h4>Severity</h4>
                    <h2>{result['severity']}</h2>
                </div>
                """, unsafe_allow_html=True)
            with col3:
                st.markdown(f"""
                <div class="metric-card">
                    <h4>Corrected DTI</h4>
                    <h2 style="color: {'red' if result['corrected_dti'] > 45 else 'black'}">{result['corrected_dti']:.2f}%</h2>
                </div>
                """, unsafe_allow_html=True)
            with col4:
                st.markdown(f"""
                <div class="metric-card">
                    <h4>Income Variance</h4>
                    <h2>${result['corrected_net_rental'] - lender_net:.2f}</h2>
                </div>
                """, unsafe_allow_html=True)

            st.write("") # Spacer

            # --- MIDDLE ROW: Explanations ---
            st.markdown("### 🧠 Agent Chain of Thought & Explanation")
            
            exp_col1, exp_col2 = st.columns([2, 1])
            
            with exp_col1:
                with st.container(border=True):
                    st.markdown("**Calculation Logic:**")
                    st.info(result['explanation'])
                    
                    st.markdown("**Defect Definition:**")
                    # Color code the definition box based on result
                    if result['defect_code'] == "PASS":
                        st.success(f"**{result['defect_code']}**: {result['severity_desc']}")
                    else:
                        st.warning(f"**{result['defect_code']}**: {result['severity_desc']}")
            
            with exp_col2:
                with st.container(border=True):
                    st.markdown("**Policy as Code Execution**")
                    st.success("✅ OPA Policy Checked")
                    for rule in result['rule_references']:
                        st.markdown(f"- 📖 *{rule}*")

        else:
            st.error("Audit failed. Check backend logs.")
else:
    # This shows when the page first loads before the button is clicked
    st.info("👈 Select a Scenario from the sidebar and click **Execute Agentic Audit** to begin.")
