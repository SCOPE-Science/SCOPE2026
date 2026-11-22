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

Run `python3 verify_exhaustive.py` and `python3 verify_formula.py` using a standard Python 3 interpreter. Both scripts are included completely with this result. The first directly enumerates extended states and maps complete attraction basins; the second independently sums the disjoint leaf-type classes to reconstruct all formulas and boundary cases. The observed outputs agreed on leaves 1 through 6 and on all symbolic summations checked for leaves 1 through 30.

The all-size result is proved by invariant reduction and closed sums in `RESULT.md`; brute-force testing of finite cases alone is not an all-size certificate. No external certification or independent audit has been performed.
