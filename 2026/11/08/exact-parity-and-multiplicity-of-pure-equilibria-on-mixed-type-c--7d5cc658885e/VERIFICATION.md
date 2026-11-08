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

Run `python verify.py` with Python 3 and no external dependencies. The script uses exhaustive direct utility-sign checks for all \(1\le a,b\le5\), for all possible conformist counts on both sides, to compare 400 distinct side-composition cases and 102,400 action profiles against the theorem's closed expression. It separately compares the random-type no-equilibrium probability by exact binomial aggregation for 64 pairs of side sizes in \(1\le a,b\le8\), using rational arithmetic. Its expected success output contains `VERIFIED` lines for these counts.

The proof of the unbounded result is the exhaustive four-case argument in `RESULT.md`; the finite computation is a consistency check and cannot independently certify the infinite assertion. The uploaded package is self-reviewed only. Independent audit and external validation have not been performed.
