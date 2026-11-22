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

# Checks and reproducibility

The analytical proof in `RESULT.md` uses elementary half-base refinements, the positive eigenvector of an explicit two-state transfer matrix, Hausdorff covers, and the entropy/dimension relation for stationary equal-ratio graph-directed measures. These steps, not experiments, support the unbounded base and time ranges. Run `python3 CHECK.py` from the directory containing this document; the script needs only the Python standard library. The recorded run compared 756 exact sign-word multiplicities for bases 2 through 7 and word lengths 1 through 6, 30 Perron-eigenvalue approximations, and six base-specific midpoint/near-endpoint dimension pairs. All executed checks passed. The script tests finite premises and is not an exhaustive proof of the Hausdorff theorem. Independent audit has not been performed.
