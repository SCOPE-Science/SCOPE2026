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

# Reproducible checks

Run `python3 verify.py` with Python 3.10+ and SymPy installed. The supplied execution produced `PASS: 106 exact symbolic checks; no assertion of exhaustive numerical verification`. It verifies the sum/difference polynomial identities, the explicit pair formulas at rational steps on both sides of the sharp thresholds, the derivative-product identities, the exact algebraic fold and flip parameters, and the three fixed points and their local multiplier inequalities at sample steps. The proof in `RESULT.md` handles all real positive step parameters; sampling and symbolic evaluation at finitely many values are supplementary only. There has been no independent validation.
