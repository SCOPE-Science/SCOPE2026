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

# Reproducibility and mathematical verification

The standalone checker `checks/check.py` uses only Python's standard library and was executed from the included package. Its output was `CHECKS_OK 17378`. It checks the displayed pointwise generalized Aluthge formula and its iteration at selected positive parameters, the exact spatial-dilation equivalence, and the critical-point maximum for consecutive differences and self-commutators. It also constructs normalized finite-window eigen/adjoint-eigen witnesses for the interior spectral disk in both parameter orientations.

These computations are finite tests. They do not establish infinitely many eigenvalues, the full Fredholm essential spectrum, strong-star convergence, or a norm limit. Those assertions are proved in `RESULT.md` using the explicit unitary transformations, spectral recurrences and functional-analytic arguments. No computer-assisted infinite certification or independent audit is claimed.
