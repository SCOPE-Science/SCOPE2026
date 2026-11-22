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
Execute `python3 check_cycle.py` using the Python 3 standard library. The checker enumerates the distinct signed-incidence vertices directly, obtains their entire Euclidean squared-distance histogram for \(3\le n\le8\), and matches it against the transfer-matrix coefficients. It independently constructs an integer-polynomial recurrence and compares complete coefficient arrays through order ten, then verifies coefficient totals, parity, both exact moments and diametral counts through order forty.

Observed reproducibility markers: `CYCLE_ZONOTOPE_VERTEX_DISTANCE_EXACT_PASS` and `CYCLE_ZONOTOPE_RECURRENCE_MOMENTS_PASS 38`.

The proof for every \(n\ge3\) is in `RESULT.md`. The finite computations do not constitute an infinite-dimensional certificate and neither experiment nor self-review is an independent mathematical audit.
