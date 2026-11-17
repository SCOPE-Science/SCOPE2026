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

# Verification record

The result is proved by explicit Euclidean geometry, an absolute positive gap \(p^2+q^2<1\), an anisotropic local scaling, and exact integration of the limiting domain. The constant \(8/15\) is twice \(B(2,3/2)\), not an experimentally inferred normalizer. Total variation follows from \(L^1\) convergence of conditional indicator densities on one bounded scaled support.

Standalone diagnostic: `check_obtuse_fagnano.py`, with dependencies `numpy` and `scipy`. For a parent with \(A=120^\circ\) and \(b=c=1\), the computed coefficient is \(1.3179485337782688\). Direct integration of the exact perimeter under Sobol sampling produced ratios 0.9045102, 0.9592424, 0.9830746, 0.9931334 at thresholds 0.025, 0.01, 0.004, 0.0016. These support consistency, but are neither exhaustive nor independent proof. The checker uses a fixed deterministic pseudorandom seed and one-dimensional adaptive numerical quadrature.

No computation is needed for the general infinite limit. Publication priority is provisional; no independent audit has been performed.
