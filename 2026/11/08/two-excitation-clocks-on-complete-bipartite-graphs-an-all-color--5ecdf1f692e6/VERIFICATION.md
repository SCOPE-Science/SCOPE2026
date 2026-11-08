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

The finite labelled-state verifier constructs each synchronous Greenberg–Hastings transition directly, removes strictly transient states by indegree peeling, and computes least periods on the remaining directed cycles. It compared the predicted period populations for 83 triples of shore sizes and color counts, covering 1,095,764 labelled states. Every comparison passed.

A separate support-based verifier iterates the graph of possible color-presence masks; 349,504 mask pairs were checked for color counts from three through nine. It found only the predicted possible recurrent masks and three extra empty-shore support masks, which are not realizable for positive shore sizes (the both-resting support mask represents the unique fixed configuration). Both programs and their outputs are included.

These computations test but do not prove the all-parameter claim. The proof uses time-periodic excitation indicators, the backward implication to a two-time parity schedule, and explicit cyclic phase motion. No independent scientific validation was performed.
