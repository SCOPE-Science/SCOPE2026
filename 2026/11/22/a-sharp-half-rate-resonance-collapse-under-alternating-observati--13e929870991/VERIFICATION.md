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

The proof reduces the firing recursion to an exact two-phase transition table including all boundary equalities. This is a complete real-parameter proof; a finite checker is not being used to infer an infinite statement.

Run `python checker.py` with Python 3 and no third-party dependencies. This verifies both initial phases on 125000 rational triples and exact resonance/boundary cases. The checker confirms temporal periods and orbit lengths via rational arithmetic; it does not test non-rational parameters, which are covered analytically.

The main premises are the forward-projection threshold/reset semantics and positive reset-to-threshold travel time. Other firing conventions can differ. No independent scientific audit has been performed.
