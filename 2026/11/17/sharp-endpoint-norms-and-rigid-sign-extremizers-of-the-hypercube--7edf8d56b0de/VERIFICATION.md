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

# Reproduction and evidence

Run `python3 verify_hodge_cube.py` from the directory containing the companion file. This program uses only the Python standard library and exact rational arithmetic. It independently calculates the orthogonal edge-transfer matrix from Walsh eigenvectors and from the dipole resolvent integral, then verifies equality of entries. Its canonical-row tests run for dimensions one through seven; full-matrix comparisons run through dimension four. It checks the Poisson equation, strict sign pattern, the per-direction absolute masses, and the exact signed input witnesses.

Executed diagnostic output includes:

```text
GREEN_VS_WALSH_CROSSCHECKS_PASSED 1954
RIGID_SIGN_WITNESS_CHECKS_PASSED 7
ALL_EXACT_HYPERCUBE_HODGE_PROJECTION_CHECKS_PASSED
```

The universal all-dimensions theorem and full equality classification are proved analytically in RESULT.md; finite computations supply independent algebraic cross-checks but are not infinite-dimensional certificates. An external independent mathematical audit has not been conducted.
