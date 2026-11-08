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

Run `python3 check.py` with Python 3 and no external libraries. The supplied checker uses exact rational arithmetic. It independently enumerates every permutation of orders 2 through 7, separately accumulates the joint major-index/consecutive-pattern moments, verifies the exact formula and both equality characterizations, and also checks the combinatorial ascent inequalities through pattern length eight and the positive algebraic identity on a larger integer grid.

The observed result was `PASS 128362 exact assertions`. The exhaustive finite checks do not establish a universal theorem on their own; that conclusion is supplied by the written conditional-probability and ascent-charging proof. No independent external audit has been performed.
