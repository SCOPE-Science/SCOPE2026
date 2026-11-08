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

# Reproducibility and limits

Run `python3 verify_cubic_cycle.py` with a standard Python 3 interpreter. A complete successful replay prints `VERIFY_OK spectral_checks=121600 factor_checks=243200 matrix_fourier_checks=9144`. The verifier uses ordinary floating-point Fourier evaluations with stated numerical tolerances, not certified interval bounds; it compares both factorizations, all discrete Fourier nodes on 200 sixfold cycle sizes, and finite matrices on seven sizes. The algebraic Lagrange-interpolation extremal certificate and the trigonometric node separations in `RESULT.md` constitute the proof for every eligible size; finite replay is not an exhaustive size proof.

The result assumes finite real symmetric row-stochastic matrices, self-holding and three circular jump classes on cycles of size \(n\ge12\) with \(6\mid n\). It does not establish unique arbitrary non-circulant optimizers, classifications for other congruence classes or mixing-time constants. Publication priority may depend on specialist sources not located in the inspected literature.
