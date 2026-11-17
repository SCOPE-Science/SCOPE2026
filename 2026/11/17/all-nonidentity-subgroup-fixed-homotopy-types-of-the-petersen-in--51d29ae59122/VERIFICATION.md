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
# Verification procedure

The included `verify.py` uses only the Python 3 standard library and regenerates `census.json` with `python3 verify.py --certificate census.json`. The program checks all 120 permutations, all 156 generated subgroups (19 conjugacy classes), both independent induced-cycle predicates on all 1,024 Petersen vertex subsets, every orbit-simplex, and each collapse step. It checks the fundamental-group elimination of the exceptional two-dimensional residual by triangle boundaries and validates the five nonidentity counts. The literal expected program output is in `output.txt`.

All tests are finite and exhaustive within the asserted domain. A check of finite exact code is not independent mathematical audit. No identity-subgroup conclusion is asserted. Access to some nearby full public project texts was unavailable; the novelty judgment therefore has an explicit literature-access limitation.
