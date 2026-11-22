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

Verification uses the two included executable programs on the actual delivered source files. `check_symbolic.py` reconstructs the three-orbit count-tilted generator symbolically and confirms its determinant, first and second cumulants, strict-Fano difference identity, consecutive-parameter monotonicity and limiting spectral factor. `check_full.py` constructs all unordered-pair states of the original graph for twelve consecutive blade counts and solves the full stationary Poisson equation without orbit formulas. Every tested result agrees with the stated rational formula. These finite computational checks corroborate but do not prove the parameter-uniform theorem. The analytical proof in RESULT.md proves its finite-size formulas and fixed-time compound-Poisson limit. No independent scholarly audit was performed.
