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

The exact proof is in `RESULT.md`. Running `python3 verify.py` checks finite rational transition matrices and stationary moments; it additionally performs fixed-seed Monte Carlo estimates of the near-critical variance scale. The independent-in-time Gaussian surrogate and the martingale-difference coupling are proved algebraically in the result, not by relying on these finite tests. No external or independent certification has been performed.
