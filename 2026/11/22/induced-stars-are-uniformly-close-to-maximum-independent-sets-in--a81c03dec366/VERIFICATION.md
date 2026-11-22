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

# Verification and reproducibility

Execute `python3 verify.py` with Python 3.10 or later; no nonstandard packages are needed. The code enumerates every perfect pairing of distinct ordered endpoints for sizes from two through seven, checks the maximum independent set by backtracking and the earliest-finish greedy algorithm, then repeats these two independent methods in every open neighborhood. The observed gap histograms match the recorded exact integer counts; all 146598 pairing configurations pass.

The general tail inequality follows instead from explicit probabilities of a central-spanning interval and two endpoint-tail boxes, a binomial subset bound, and an elementary deterministic deletion inequality. Only these analytic arguments justify general quantifiers. The endpoint distribution must have no atoms and be common to all sampled endpoints; this check does not apply to independently sampled fixed-length intervals or dependent endpoints.

No formal proof assistant or independent expert audit has been used. No optimality of constants or unique historical priority is claimed.
