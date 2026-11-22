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

The standalone `verify.py` reconstructs the area of a natural cubic spline from the tridiagonal second-derivative relation, differentiates its exact integral with respect to nodal data, and compares the result with the claimed three weights. It additionally checks partition of unity, affine exactness, both algebraic sign boundaries, the algebraic survival-function inverse and the exact asymptotic coefficient of the squared-noise gain.

It passed 360 independent exact-rational configurations with random positive rational cell lengths and rational nodal data, verifying the exact area formula and coefficient signs. SymPy version 1.14.0 was used. The probability theorem uses the analytic uniform-ratio transformation and the explicit inversion in the proof; no finite sample establishes its validity. Positivity and tail statements apply only to the stated three iid uniform knots and normalized integration over their hull. Independent mathematical audit has not been performed.
