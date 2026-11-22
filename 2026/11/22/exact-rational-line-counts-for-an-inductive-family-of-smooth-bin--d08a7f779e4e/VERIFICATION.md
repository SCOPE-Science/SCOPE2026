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

# Reproducibility and verification

The source construction is the transformed smooth quartic \(H=B(X_0,X_1,X_2+X_3,X_2)\), *not* the untransformed quartic \(B\). Its smooth hyperplane section permits the published recursion.

Run `python3 verify_lines.py` with Python 3 standard library only. The checker independently implements homogeneous GF(2) polynomial substitution and exhaustive rank-two parameter words for \(3\le n\le7\); the exact counts are 5, 31, 147, 635, and 2635. It separately enumerates 256 base words and all 16 two-vector transfer states, verifies the five-orbit matrix, checks the exact closed expression and the first 32 coefficients of the generating function. These calculations are finite corroboration, not the proof of the infinite formula. The infinite proof is the symbolic restriction identity and exact finite-state recurrence detailed in `RESULT.md`.

The checked scientific scope does not include geometric Fano schemes, rational lines over extension fields, or independently validating every source theorem. No independent external review or audit was conducted.
