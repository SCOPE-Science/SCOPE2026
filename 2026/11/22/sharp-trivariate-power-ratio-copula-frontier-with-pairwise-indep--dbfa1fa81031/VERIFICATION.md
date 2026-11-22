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

The standalone `checker.py` was executed using exact SymPy arithmetic. It reported `0<p<=1 80 exact Bernstein coefficients verified`, `p>=1 80 exact Bernstein coefficients verified`, and `PASS: corner necessities and all 160 positivity certificates`. The script calculates the numerator from derivatives rather than assuming a stored polynomial and then checks all necessary vertex identities and complete tensor Bernstein coefficient families. The proof separately treats denominator positivity, the endpoint with a removable singularity, margins, and dependence. These finite exact computations certify stated algebraic reductions; the paper supplies the continuous-domain argument. Independent checking and historical-priority assessment remain outstanding.
