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
# Reproducibility

Run `python verification/check.py` using Python 3.10+ standard library. It computes exact rational coefficients by a polynomial dynamic program for dimensions 2 through 15, cross-checks dimensions 2 through 8 against independent ternary enumeration, verifies the full alternating-sign lower family through 100 coordinates, and checks exact finite-pair derivatives against explicit Euclidean \(\ell_1\)-ball projection on deterministic rational examples.

A completed execution printed `ALL_ANCHORED_BV_CROSSPOLYTOPE_CHECKS_PASS` after the detailed per-dimension and witness checks.

The dynamic-programming induction, all-chamber realization, and dimension-uniform upper/lower bounds are established analytically in RESULT.md; finite computations cannot certify an unrestricted theorem by enumeration. Neither historical priority nor independent mathematical validation is certified by the script.
