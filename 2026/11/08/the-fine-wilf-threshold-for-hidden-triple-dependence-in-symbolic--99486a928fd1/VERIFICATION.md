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

Run `python3 CHECK.py` using the standard library. It independently builds the undirected equality graph for every listed parameter choice, computes its cycle rank by disjoint-set union, and tests the closed three-time formula against this graph calculation. Separate tests enumerate every entire finite binary or ternary word over the event coordinates and count those satisfying the return equalities directly, without using the analytic cycle-rank formula as the counting method.

The closed-form theorem is established by the connected-component argument in `RESULT.md`, not by finite enumeration. In particular, no finite test establishes an all-integer identity or historical priority. The exact normalization is a product measure over all finite blocks intersecting the return constraints. The status above describes only the absence of an independent audit.
