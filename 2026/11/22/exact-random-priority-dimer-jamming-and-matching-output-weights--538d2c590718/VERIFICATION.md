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

# Reproducible verification

Run `python VERIFY.py` from a directory containing the attached script, using Python 3.10 or later; no third-party packages are required.

The first computation uses the edge-set recurrence on occupied-vertex bitmasks. The second enumerates **all** terminal maximal matchings and computes each one's exact arrival-priority integral, without reusing the first recurrence. It reports 257 passed exact checks, the 2,270 reachable occupied-vertex subsets, and the five matching-output classes. Every comparison is done with Python arbitrary-precision integers and rational fractions. The mathematical proof of the integral evaluation appears in `RESULT.md` and does not rely on floating-point experiments.

Verification covers the specified 14 vertices and 21 edges only. It is an exhaustive finite certificate, not evidence for any unproved statement about other graphs. Historical novelty rests on literature comparisons, not on the checker. Independent audit is not performed.
