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

Run `python verify.py` with Python 3, NumPy, and SymPy. The checker verifies exact algebraic identities for the proposed weights and bound, constructs sunlet stochastic matrices, compares their actual nonconstant eigenvalues with the formula and Fourier spectrum, and tests 3,280 feasible invariant perturbations and 770 feasible noninvariant matrices. The code is deterministic. The analytic proof in `RESULT.md` is essential: finitely many numerical tests cannot certify the theorem for all integers \(m\ge3\), all real weights, or every noninvariant feasible matrix. No independent mathematical audit is represented.
