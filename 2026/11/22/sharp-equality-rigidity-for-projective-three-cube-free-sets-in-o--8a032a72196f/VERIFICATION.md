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

# Reproducible checks

Run `python3 verify_projective_cubes.py` using only the Python 3 standard library. The script builds all seven nonempty subset sums with repeated generators and enumerates all sets of the target maximum size, excluding zero because it is itself a degenerate forbidden cube. It checks groups of orders 3, 9, 15 and the rank-two ternary group of order 9, verifies the threefold-shift period identity for every enumerated equality set, and tests the inverse-image construction in the group of order 27. Expected output ends in `VERIFY_OK`.

The exhaustive enumerations establish only the tested finite examples. The unrestricted bound, quotient reduction and exact rank-one/rank-two classification follow from the mathematical proof in `RESULT.md`. Neither the script nor its output constitutes an independent audit.
