from langgraph.graph import StateGraph, END
from typing import TypedDict

class AuditState(TypedDict):
    loan: dict
    result: dict

def rental_audit(state: AuditState) -> AuditState:
    loan = state["loan"]
    
    # 1. Rental Math
    adjusted_rent = loan["gross_rent"] * 0.75  # FNMA 75% vacancy rule
    corrected_net = adjusted_rent - loan["pitia"]
    variance = corrected_net - loan["lender_net_rental"]
    
    # 2. DTI Math
    total_income = loan["borrower_income"]
    # New DTI = (Total Obligations + True Rental Loss) / Income
    # If rental is positive, it adds to income instead of obligations (simplified for demo)
    if corrected_net < 0:
        corrected_obligations = loan["total_obligations"] + abs(corrected_net)
    else:
        corrected_obligations = loan["total_obligations"]
        
    corrected_dti = (corrected_obligations / total_income) * 100
    dti_variance = corrected_dti - loan["submitted_dti"]
    
    # 3. Defect Classification & Explanation
    explanation = f"1. Applied 75% factor to Gross Rent (${loan['gross_rent']} * 0.75) = ${adjusted_rent:.2f}\n"
    explanation += f"2. Subtracted PITI/A (${loan['pitia']}) = Net: ${corrected_net:.2f}\n"
    explanation += f"3. Variance vs Lender (${loan['lender_net_rental']}): ${variance:.2f}\n"
    
    if abs(variance) < 1.0: # Close enough (float math)
        defect_code = "PASS"
        severity = "None"
        severity_desc = "Loan calculation is accurate. No defects found."
    elif variance > 0:
        defect_code = "RENT-001"
        severity = "High" if corrected_dti > 45 else "Medium"
        severity_desc = "Income Overstatement. Lender claimed less rental loss or more rental income than permitted."
    else:
        defect_code = "RENT-002"
        severity = "Critical" if corrected_dti > 45 else "High"
        severity_desc = "Loss Understatement. Lender hid the true cost of the rental property, artificially lowering the borrower's DTI."

    if corrected_dti > 45.0:
        explanation += f"\n🚨 CRITICAL: The corrected DTI of {corrected_dti:.2f}% exceeds the 45% maximum threshold. This loan is ineligible for purchase."

    state["result"] = {
        "corrected_net": corrected_net,
        "variance": variance,
        "corrected_dti": corrected_dti,
        "dti_variance": dti_variance,
        "defect_code": defect_code,
        "severity": severity,
        "severity_desc": severity_desc,
        "explanation": explanation
    }
    return state

workflow = StateGraph(AuditState)
workflow.add_node("audit", rental_audit)
workflow.set_entry_point("audit")
workflow.add_edge("audit", END)
app = workflow.compile()

