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

The standalone `verify.py` implements direct period-wide testing of all consecutive factors and independently counts maximal cyclic clusters for eighteen parameters between 2 and 20. It also checks the exact least period, weighted counts and support dichotomy, plus algebraic formulas for every integer \(2\le k<2000\). Execute `python3 verify.py` using the standard library.

The unbounded statement follows from the proof's CRT argument and the explicit boundary construction, not from finite enumeration. In particular, no claim is made about first admissible endpoints, their initial-interval frequency, or a resolved conjecture. Independent mathematical audit has not been performed.
