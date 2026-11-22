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

The all-size theorem is proven by direct ground-state enumeration, Dirichlet symmetry decomposition, the rank-one resolvent and a binomial concentration expansion in `RESULT.md`.

The standalone pure-Python `verify.py` checks the legal ground-state generator against its exact two-level reduced representation for every state and each reduced basis coordinate at \(n=2,3,4,5,6\). It independently reconstructs the binomial resolvent formula using eight exact-rational linear solves at \(n=2,3,4,5\). Its actual successful output is:

`FRIENDSHIP_EXACT_CHECKS_PASSED ground_states= 2178 resolvent_cases= 8`

The optional `numerical_check.py` requires NumPy and SciPy; it explicitly diagonalizes all \(2\cdot3^n\)-state generators for \(n=2,3,4,5\) and compares their lowest nonzero eigenvalues against the scalar secular root. Maximum absolute discrepancy among the four cases was below \(9\cdot10^{-15}\).

Finite checks cannot rule out general-parameter logical errors without the proof, and independent mathematical review is not yet performed. No positive-temperature dynamics is claimed.
