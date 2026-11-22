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

# Reproducibility checks and scope

Execute `python verify.py` using Python 3 and only its standard library. Its fixed random seed makes the check deterministic.

The actual execution returned `ALL_CHECKS_PASSED`, with 56 verified unit-radius gap-area cases, 12 independent radial-integration comparisons, 12 finite-size scaled-area checks (three radius-window parameters across four sizes) and 30,000 simulated circular-center configurations checking two classical spacing probabilities. The numerics have finite precision and sample error. They do **not** establish a theorem for arbitrary \(n\), a convergence rate, or historical priority.

The mathematical evidence is the closed-form conditional circular-spacing survival function, exact two-endpoint disk inequality (1), collapsing negative half-plane argument, convergence of convex compact sets and directly integrated limiting vertical sections in `RESULT.md`. No external solver or independent mathematical audit is required for or claimed by this reproducibility script.
