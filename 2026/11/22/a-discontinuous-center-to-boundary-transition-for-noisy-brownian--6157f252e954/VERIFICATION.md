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

The proof evaluates the bridge covariance for a uniform window average, reduces the gain to a ratio of a quadratic and a positive affine function in squared center displacement, and proves that its derivative numerator is strictly increasing. This excludes all interior optimal displacements before the boundary comparison is made. An exact factorization establishes the critical exposure and noise levels, including all equality cases.

`python verify.py` (Python 3, SymPy, mpmath) replayed the three-region covariance integral, four exact polynomial identities, the critical-width and critical-noise equations, exact rational examples and 16 numerical quadratures using the original covariance kernel. Finite checks corroborate the expressions; the elementary sign proof provides the all-parameter guarantee. No claim is made for other kernels, adaptive schedules, or independent mathematical review.
