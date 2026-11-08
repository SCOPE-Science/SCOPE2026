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

Run `python3 verify.py` from the extracted package. It uses only Python's standard library and exact rational arithmetic, verifies moment-generating-function coefficients independently against all ordered positive compositions for total sizes 2–9, and evaluates the exact rational generating-function recurrence for every size 1–100. It confirms covariance zero at 1 and 2, strictly positive at sizes 3–14, strictly negative at 15–100, plus the sharp values at 14 and 15. It also checks that the explicit coefficient-wise complex-analytic tail bound at size 100 is smaller than 4/189; because its constituent \(n(2/3)^n\) terms decrease for sizes 100 and above, the proof covers the infinite remaining range. The generating-function decomposition and the Cauchy estimate remain mathematical proof obligations documented in RESULT.md, not claims certified merely by finite enumeration.
