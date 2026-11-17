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

# Reproducible checks and limits

Run `python3 verify_rigid_occupation.py` in the same directory as this document. It requires only Python 3 standard-library modules and produces `RIGID_QUARTIC_OCCUPATION_MOMENTS_OK` if its finite tests pass. The checks cover the exact radial primitive, the inverse-function relation, representative conserved levels, the limiting survival prefactor, and two moment-scaling comparisons at positive but small boundary distance. In separate symbolic differentiation, the derivative of the displayed closed form of \(J\) simplified exactly to \(-1/[r^2(b+ar^2)]\). The theorem's all-parameter and asymptotic assertions are supported by the analytic proof in `RESULT.md`, not by extrapolation from the finite tests.

All quantitative constants use the exact invariant-coordinate normalization \(\delta=C-1\) and the original physical clock \(\dot\theta=1\). The missing full text of the 2015 nonhomogeneous quartic phase-portrait article is a literature-priority limitation, not a mathematical verification failure. Independent mathematical audit: not performed.
