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

The analytic proof reduces the holomorphic functional calculus to two Taylor coefficients and proves the determinant identity \(\det(3I-H(x))=6x(1-x)\). Schwarz–Pick supplies the coefficient constraint. The expansion near the quadratic monomial has squared-norm deficit \(6s-4x+O(s^2)\) where \(x\le s\), while the linear monomial has deficit \(3h+O(h^2)\). A degree-two Blaschke family realizes both limiting constants exactly. These are mathematical arguments applying to all scalar Schur functions, not extrapolations from enumeration.

Run `python check_critical_nilpotent.py` with Python 3, NumPy and SymPy to replay 3,975 independent diagnostic assertions. Finite diagnostics are only auxiliary checks; there is no independent mathematical audit.
