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

The exact interior-volume and coordinate-covariance identities follow from the displayed unit-simplex monomial integrals, the known forbidden-set description of parity polytopes, and invariance under even coordinate complementation. The disjoint-corner argument is an all-dimensional proof, not a finite enumeration.

Run `python check_demicube.py`. The checker uses `fractions.Fraction` for the dimension-five global-minimum threshold, base values, cube comparisons, and a finite range of consecutive variance comparisons. It optionally performs an independent floating-point `scipy.spatial.ConvexHull` reconstruction of the hull volume for dimensions three through six; this last cross-check is explicitly numerical. A successful run on the package files gave `DEMICUBE_ISOTROPIC_EXACT_CHECKS_PASSED` and `DEMICUBE_CONVEX_HULL_VOLUME_CHECKS_PASSED`.

For the unbounded dimensional quantifier, the proof relies on the exact deficit ratio inequality, the strictly increasing coordinate variance for all dimensions at least five, and the dimension-seven rational barrier. A finite checker cannot establish these universally quantified inequalities. The asymptotic limit follows by first-order expansion of the closed formula. Mathematical historical priority is provisional; no independent audit has been performed.
