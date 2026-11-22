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

`CHECK.py` is a standalone standard-library Python 3 supplementary checker. Run `python3 CHECK.py` from this directory. It passed 9,675 assertions covering 1,610 fixed-marginal pairs (including ten preselected edge/balance examples), independent root-solving of the inverse log-odds relation, the exact root of the reciprocal curvature derivative, strict and equality marginal bounds, and randomized finite pairs of log-kernels. Five representative marginal pairs also undergo three sizes of infinitesimal checkerboard perturbations, approaching the analytically computed sharp operator norm.

The checker is finite and uses floating-point arithmetic. It is not a proof of the universal assertions or of novelty. The proof in `RESULT.md` establishes the global maximum-entry bound, exact sharpness and all boundary/equality cases using strict convexity, a scalar implicit function, and derivative integration. The cited source inspection distinguishes previously known pointwise implicit derivatives from the optimized global coefficient. Independent external mathematical validation and historical-priority certification have not been performed.
