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

The accompanying `checker.py` performs fresh algebraic stationarity, trace, block-determinant and concurrence-branch checks, and independently constructs the full complex Liouvillian from matrix units on 72 parameter triples. It compares the stationary solution against the closed formula, tests positivity, verifies the unique numerical zero mode in the selected samples, and computes Wootters concurrence independently. The checker passed 442 assertions with Python 3.10+, NumPy and SymPy. No finite sample is used to establish the all-parameter theorem; exact algebra and the faithful-stationary-state commutant proof provide that foundation. Independent scientific audit has not been performed.
