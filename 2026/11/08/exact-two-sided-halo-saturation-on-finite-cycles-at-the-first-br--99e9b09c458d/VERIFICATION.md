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

# Reproducible checks and limits

The included `VERIFY.py` is a standalone standard-library program. Run `python3 VERIFY.py` to repeat an independent integer-bitmask enumeration of all circular arcs and marked sets for orders 3 through 14, tests of the sharp consecutive-block construction for all orders through 200, and even-cycle alternating thresholds through 100.

Observed output:

`VERIFY_OK exhaustive_orders=12 contiguous_constructions=198 checkerboard_thresholds=49`

The program uses integer inequalities throughout, so no floating point comparisons determine halo membership. A computational census over finitely many orders cannot prove the assertion for arbitrarily large cycles; the proof of that assertion is the two-cover lemma, cardinality summation, parity obstruction, and explicit upper-bound construction in `RESULT.md`. This verification does not establish historical priority or independent external certification.
