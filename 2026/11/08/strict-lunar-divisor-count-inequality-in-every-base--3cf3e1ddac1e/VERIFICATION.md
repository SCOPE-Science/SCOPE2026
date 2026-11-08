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

The theorem is proved for all integer bases and positive integers in `RESULT.md`. The accompanying Python 3 checker runs `python3 verify_lunar.py` and performs a completely independent finite enumeration of dismal factor pairs, divisor sets and digitwise sums.

Observed output:

`VERIFY_OK bases=2..10 inputs=1019 products=47489 missing_witnesses=974 all_strict_for_n_gt_one=PASS equality_only_n_one=PASS unit_divisor_sum=PASS`

The checker confirms the inequality, equality only at one, the one-digit formula and the explicit missing units-digit witness for all tested cases. Its finite coverage is not a substitute for the proof. Historical novelty is not independently certified.
