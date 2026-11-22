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

The proof derives the conditional Rayleigh survival law, then invokes strict convexity of two exponential transforms to prove a single cumulative-tail crossover and exactly two extrema for all positive nonconstant finite-mean stopping laws. No finite enumeration is used to prove infinite-law assertions.

Run `python3 check_single_crossing.py`; its deterministic diagnostic suite passed 6,800 assertions. The code relies only on the Python standard library and includes discrete laws with widely separated retention times, a two-level exact algebraic example and weak-heterogeneity limit tests.

Validity limits: unbounded retention laws require finite mean but not finite inverse moment; independence from carrier movement and isotropic planar diffusion remain essential. Checks do not establish historical priority, species calibration or relevance to non-Gaussian movement.
