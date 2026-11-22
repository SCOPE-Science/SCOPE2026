---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The standalone `check.py` uses only Python’s exact rational arithmetic. It verifies four strict derivative-sign inequalities and, independently, solves the full discounted hitting-probability linear system at two rational survival parameters. It passed on the stated rational rates without floating-point tolerances. The proof then uses exact polynomial continuity and analytic sign change; finite checks certify the four exact evaluated values but are not an exhaustive root count.

Strictly positive transition probabilities and positivity of both subchain killed resolvent determinants are proved analytically. Historical priority is assessed only against inspected sources and accessible search evidence; no independent audit was conducted.
