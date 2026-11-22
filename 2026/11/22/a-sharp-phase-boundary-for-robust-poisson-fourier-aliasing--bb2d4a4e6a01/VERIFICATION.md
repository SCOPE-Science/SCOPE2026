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

Run `python3 verify.py` with Python 3 standard library and no external input. The checker uses a fixed random seed. It directly evaluates inverse-Cauchy quantiles and the sampled density ratio; the numerical shift integration is performed independently of the analytic spectral expression. It also tests location and scale endpoint constraints, off-center references, both optimizer branches, and finite positive mixtures. The recorded execution completed `PASS 15968 checks`.

The algebraic proof in RESULT.md, not the finite checker, establishes assertions for all parameters, all node counts, and all Borel positive mixtures. Mathematical priority outside the inspected literature and independent proof review remain unverified.
