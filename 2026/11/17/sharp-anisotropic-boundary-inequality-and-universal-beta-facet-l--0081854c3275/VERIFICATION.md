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

All finite checks were run using the included `verify.py`, with exact SymPy rational determinants and no floating-point tolerance. The 270 tested facet Gram determinants and the associated volume determinants agree for parameters \(2\le m\le6\) and three independent positive rational scale pairs. The output was `CYCLE_ANISOTROPIC_PASS cases=270 m=2..6 distinct_scales=3`.

The complete general claim rests on the explicit free-sum coning, a cycle-incidence singular-value product, all-parametric normals, the Euclidean pyramid-volume identity, the paired vector triangle inequality, and a uniform Riemann-sum estimate. Finite determinant checks do not establish any infinite statement by themselves. No independent mathematical audit has been conducted.
