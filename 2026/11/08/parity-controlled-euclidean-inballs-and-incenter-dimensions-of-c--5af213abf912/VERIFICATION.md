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

Run `python verify.py` from the same folder with NumPy and SciPy. The run reported:

`BICLIQUE_INBALL_FACETS_CENTERS_CHECKS_PASSED 17`

The program constructs genuine signed edge vertices, builds independent sign potential facet normals, verifies sharp support inequalities, computes the complete maximum-normal rank, and solves unconstrained-center ball linear programs. At small ambient dimension the convex hull's facets are independently obtained by Euclidean `ConvexHull` rather than by the sign construction; their complete distance multiset is compared to the formula. The full algorithm checks positive nonzero perturbations in every predicted incenter-space direction. It also checks the exact balanced-even segment endpoints for block sizes 2, 4 and 6, including the duplicate-facet exception at size 2. The tested parameter pairs have `2<=p<=q`, `p<=5`, `q<=7`, `p+q<=11` (17 pairs).

The infinite integer family is proved analytically in `RESULT.md`. The finite checker is not an exhaustive search over all parameters and is not an independent mathematical audit. In particular historical novelty remains provisional.
