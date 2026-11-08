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

# Reproducible checks

The standalone `check_one_sided.py` uses Python standard-library `math` functions and bisection to solve the two exact optimizer equations and evaluate the analytic frame-bound functions after common normalization. Its comparisons are at four integer redundancies, not a proof over all positive integers. The numerical output should end with `ONE_SIDED_GABOR_ASYMPTOTIC_CHECK_PASS orders=4`.

The mathematical proof uses the uniform hyperbolic expansions and the cited published theorem guaranteeing that each critical root is the unique global optimizer. The leading regret follows from the second derivative and Taylor's theorem, not from fitting finite observations. No external or independent audit has been performed.
