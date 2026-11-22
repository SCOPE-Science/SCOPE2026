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

# Reproducibility checks

Run `python verify.py` with Python 3.10 or later and the standard library only. A successful run prints `VERIFY_OK` with `models_checked= 92314` and `cases= 19`.

The script computes the rank directly by repeatedly evaluating the modal formula on the surviving set of worlds. Separately it computes rank by simultaneous row/column sink removal. It verifies equality for every valuation of 19 small grids (including all 65,536 valuations of a 4-by-4 grid); it also compares every coefficient of the stated polynomial recurrence with direct rank counts, and checks the rank-zero expression, sharp maximum and its exact multiplicity, two-row coefficient list and directed checkerboard test for nonempty terminal outcome. The independent enumeration is finite and is not used as an all-size proof.

The general proof is in `RESULT.md`. No formal proof-assistant certificate or independent external mathematical audit is claimed.
