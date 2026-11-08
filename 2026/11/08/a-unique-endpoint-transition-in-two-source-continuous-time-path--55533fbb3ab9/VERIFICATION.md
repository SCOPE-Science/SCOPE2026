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

# Verification

From the same folder, execute `python3 verify_deadline.py` with Python 3. The checker independently constructs the full finite-state infection CTMC (rather than only the derived gap formula), evaluates the completion probability by uniformization, and tests it against the product of Poisson survival functions. It exhaustively compares all seed pairs on a finite grid of path sizes and deadlines and checks the claimed endpoint sign criterion, the coefficient-sign structure, and strict small-network examples. Check output gives the number of successful assertions.

Analytical arguments in RESULT.md, not the finite tests, establish the conclusions for all \(n\ge2\), \(t>0\) and \(\lambda>0\). The checker uses 72-digit decimal arithmetic for positive-time evaluations and exact rational arithmetic for coefficient ratios; finite-precision tests cannot prove equality at a transcendental critical deadline. An independent audit or external validation has not been performed.
