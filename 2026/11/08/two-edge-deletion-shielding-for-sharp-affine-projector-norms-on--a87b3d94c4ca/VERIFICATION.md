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

Run `python verify_two_deleted_edges_p1.py` in this directory after installing `sympy>=1.12,<2` from `requirements.txt`. The checker verifies three symbolic positive-numerator identities with no finite-q cutoff, reconstructs exact inverse Gram matrices and edgewise kernel integrals for q=1,...,7, and proves the two asymptotic constants by symbolic limits. Successful output ends with `ALL_TWO_DELETED_EDGE_SPLINE_PROJECTION_CHECKS_OK`. Finite matrix examples independently corroborate the analytical proof; no external certification or independent audit has been performed.
