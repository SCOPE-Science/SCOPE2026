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

# Reproducibility and verification

Run `python3 VERIFY.py` with standard-library Python 3 from the directory containing the included files. An intact copy prints `VERIFY_OK 688 exact-rational checks`. The checker tests positive definiteness through exact determinants, direct inverse evaluations of quadratic objective values, exact meeting of both undamped rays, exact damped distance contraction, the balanced ratio and its sharp spectral boundary, and the unbalanced family for several rational parameter choices. The source code and all data needed for these checks are included; no network access or extra dependency is needed.

The exact algebra in RESULT.md independently proves the theorem for all allowed real matrices, damping values and contrasts. Finite checks do not prove the universal statements, exclude all counterexamples or establish novelty. The original work's optional safeguards and finite-precision operation are outside the result. Independent mathematical audit has not been performed.
