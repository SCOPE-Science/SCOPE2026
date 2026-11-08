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

The analytic proof establishes the result for arbitrary finite positive-integer periodic branching sequences, rather than by enumerating cases. Reproduce supplementary finite checks with `python checker.py` (requires NumPy and SciPy); execution on the packaged source returned `PASS: 637 supplementary finite assertions`.

The checker verifies Perron left/right vectors, singular zero at the geometric-mean radius, numerical convergence of finite-section smallest singular values, first-order critical slopes, and strict period-four branching-order formulas. Finite tests cannot certify equality across all Hilbert-space vectors or exhaust the continuous parameter; the proof in `RESULT.md` supplies those steps.

The sharp onto right-inverse bound is meaningful only off the critical circle. The spectral description and general shift-channel decomposition have known antecedents. Independent mathematical review has not been performed.
