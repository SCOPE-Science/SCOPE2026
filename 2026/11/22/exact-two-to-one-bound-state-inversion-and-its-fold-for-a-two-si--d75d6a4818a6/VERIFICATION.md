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

# Verification and scope

The direct recurrence yields \(F_{a,b}(z)=1-(a+b)z+abz^2-bz^3\) for \(\lambda=z+z^{-1}>2\). The strictly positive Birman–Schwinger edge test establishes precisely two bound eigenvalues in the stated parameter region. Factoring the cubic gives the quadratic inverse equation \(Q_{r,s}(t)=0\), and its sign at one proves both roots are admissible. The fold and its branch separations follow from exact quadratic discriminant algebra.

Run `python check.py` with Python, NumPy and SymPy to reproduce exact symbolic identities, the explicit algebraic isospectral pair, and finite-section numerical diagnostics. Mathematical completeness for all positive two-site potentials rests entirely on the displayed analytic proof, not on sampled parameter points or finite truncations. The source-priority comparison is based on published Jost/direct-spectral and full-resonance inverse theories, not on a claim of independent specialist validation.
