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

The embedded `verify_exhaustive.py` is standard-library-only. It independently enumerates all \(2^{n-1}\) height-two Dyck paths by compositions for \(1\le n\le17\), recomputes all overlapping counts for every binary word of lengths one through four, tests that observed equality and the proposed parameter equality coincide in both directions, and verifies the entire feasible tuple set.

The separate `verify_transfer.py` multiplies four truncated integer series to extract the rational generating-function coefficients through \(n=55\), compares those coefficients with direct integer tuple feasibility counting, and checks the full ten-entry four-factor table for 500 seeded random compositions with semilength at most 250.

Commands from the extracted package directory:

```
python3 verify_exhaustive.py
python3 verify_transfer.py
```

Expected terminal completion markers: `EXHAUSTIVE_OK` and `TRANSFER_AND_OCCURRENCE_OK`. Both scripts are finite checks; the exact all-length result rests on the constructive proof in `RESULT.md`. No independent audit has been performed.
