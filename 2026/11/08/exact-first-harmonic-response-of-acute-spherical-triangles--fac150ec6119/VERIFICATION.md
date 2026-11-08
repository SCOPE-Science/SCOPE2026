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

# Reproducibility

Run `python verify.py` with Python 3.10 or later. The file uses only the Python standard library, a fixed random seed, direct nested midpoint quadrature of the conditional spherical integral, and independent uniform-sphere Monte Carlo with intrinsic angle sign tests.

A successful execution returns `ACUTE_SPHERE_CHECK_OK`, numerically confirming the exact baseline, weighted cosine moment, dipole response at \(\varepsilon=0.7\), and local pinned Fisher derivative. The fixed quadrature uses 1000 conditional side-distance panels and 600 conditional longitude panels. The stochastic portion uses 550,000 independent triples and a separate pinned test from the same samples. Its tolerances are intentionally finite and do not establish exactness or exhaustive coverage.

The critical symbolic integral reduction is provided in RESULT.md, including the two inner integrals \(J_0\) and \(J_1\). The numerical verifier is supplementary, not a replacement for that argument. The complete event is defined by three strict tangent-vector dot-product tests; right-angle cases have probability zero.

No independent audit has been performed.
