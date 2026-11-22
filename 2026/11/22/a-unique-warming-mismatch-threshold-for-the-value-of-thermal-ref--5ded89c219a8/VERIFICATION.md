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

The explicit dominant-eigenvalue formula, the sign comparison with homogenization, and strict monotonicity of the critical-migration curve are proved analytically in RESULT.md.

Run the included standard-library Python script with `python checker.py`. Its fixed-seed tests check the signs on both sides of the critical movement rate across a broad positive parameter grid, the unique climate-mismatch threshold via bisection, increasing critical migration, and the small- and large-migration asymptotic coefficients. The complete local run reported `PASS: 23712 supplementary assertions`.

Numerical checks are supporting diagnostics, not certification of a continuum theorem. Independent mathematical audit and empirical validation have not been performed.
