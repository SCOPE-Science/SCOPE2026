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

The standalone `verify.py` is part of this package. Run `python3 verify.py` with Python 3 (standard library only). It checks 16 exact-rational parameter instances on both sides of the geometric transition and at the transition, including the enumerated octant vertices, facet incidence, determinant-volumes, and symbolic deficit identities. It separately checks 1,725 rational test points against exact orthogonal feet on all faces of three axially stretched octahedra.

These finite cases are diagnostics, not an all-parameters proof or independent audit. For every real positive stretch, the full proof is in `RESULT.md`: orthogonal-foot projection formula, minimization over signed faces, facet dominance, octant vertex/face enumeration, determinant volumes, factorization and smoothness calculation. The proof assumes ordinary Euclidean projections, strictly positive axis lengths and the relative-interior definition. No computations from previous reports or unbundled files are necessary.

Self-review: passed. Independent audit: not yet performed.
