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
# Reproduction and limits

Run `python3 verify.py` with standard Python 3 for exact rational tensor cubature and the crossing polynomial. It verifies 36 parameter profiles for \(q=2,\ldots,7\) and weights \(t=0,1/8,1/4,1,2,7/2\). The 299-page-count sign and polynomial checks establish finite corroboration, not an infinite theorem. If NumPy and SciPy are installed, an independent direct convex-hull integration checks eight low-dimensional cases for \(q=2,3\) and weights \(t=0,1/4,1,2\). Expected terminal markers are `EXACT_TENSOR_CUBATURE_AND_SPECTRAL_CHECKS_PASSED`, `INDEPENDENT_CONVEX_HULL_MOMENTS_PASSED`, and `BOOK_GRAPH_ZONOTOPE_CHECKS_PASSED`.

The infinite statement is proved by exact injective fiber integration and the cubic coefficient sign argument in `RESULT.md`. The optional convex-hull checks use low dimensions only because triangulation of higher-dimensional nonsimplicial facets can be numerically unstable. No external or formal certification is asserted.
