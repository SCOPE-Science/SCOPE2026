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

Run `python verify.py` with the packages described by `requirements.txt`. The checker directly generates stable subsets of the odd-cycle graph plus clique singleton vertices; tests the complete candidate H-description and dimensions of all facets; solves the unrestricted Euclidean ball linear program; and compares its center and optimal radius with the analytic formulas and active contact orbits. It includes each side of the boundary and exact critical examples. It successfully returned:

`ODD_WHEEL_JOIN_INBALL_CHECKS_PASSED 24 5058 654`

The counts are 24 tested parameter pairs, 5,058 generated stable-set vertices counted across examples, and 654 facet-rank checks. Comparisons use floating-point tolerances, and only finitely many parameter pairs are run; these computations do not constitute an all-parameter proof. The analytical proof and the original established odd-cycle facet theorem provide the infinite argument. No independent mathematical audit is asserted.
