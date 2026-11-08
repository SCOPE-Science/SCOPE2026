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

# Verification of original equations

The companion `verify_mixed_pairs.py` enumerates full matrix spaces over prime fields and tests `P*P==P`, `N*N==0`, and `P*N==0` directly. It checks each joint rank cell, not just the total. The test file `verify_output.txt` contains the exact output from the program executed on the packaged source. The program also verifies every proposed dimension and maximal-rank profile through dimension 40 by finite integer optimization. It is a reproducibility aid and not a proof for all fields or dimensions.

Verified direct equation cases: (n, p)=(1,2),(2,2),(2,3),(3,2),(3,3). The total pair counts for these cases are respectively 2, 17, 46, 415, 5020. The terminal success line is `MIXED_PAIR_DIRECT_CHECK_PASS`.

The mathematical proof uses square-zero flag data, complements of subspaces, a positive-definite quadratic bound, and rank-stratum closure arguments. A separate independent mathematical audit has not been performed.
