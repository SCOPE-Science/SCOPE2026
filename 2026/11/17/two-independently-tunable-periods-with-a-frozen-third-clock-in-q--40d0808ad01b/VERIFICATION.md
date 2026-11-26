---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For strictly disjoint circles the angular speeds are f3 B on the inner-center circles and −λ f1 f2 on the off-center circle; each has constant nonzero sign in the stated large-positive-γ neighborhood. Reciprocals of absolute speeds therefore give least physical-time periods, including the exactly frozen third period. The cofactor on Ci is 2λy(r_i²−r_j²); pairing the two angles with opposite sine in its time integral leaves a nonzero constant times β times a strictly positive integral of sin². On C3 the cofactor is 2yB, and its time integral leaves only the βy² term, because its speed depends only on cosine. These nonzero cofactor integrals prove transverse hyperbolicity. The cubic part of A is (x²+y²)((2λ−α)x−βy), giving exact quartic degree. Differentiating under the integral gives the two derivative columns with leading rows −γ^(−2) I(r)(ρ(r),1). To verify injectivity across all admissible branches, subtract the quadratic equations for a proposed common ρ at distinct radii: (r₂²−r₁²)(1−ρ)=0, but substituting ρ=1 requires s=0. The determinant is hence eventually nonzero with the stated sign and scaling, and the inverse-function theorem applies on the open hyperbolic region. Independent direct midpoint quadrature and central differencing gave periods (0.72101547737624, 0.95716091637545, 13.62997409314272) and determinant −0.00138203376 at the representative point. At γ=2000 the ratios of the scaled determinant to its claimed limit were 0.99969, 0.99576, 0.99100, 0.97705 across the four geometries in check.py.

## originality

PASS

The supported distinct contribution is the rank-two submersion for every admissible fixed two-concentric geometry while the off-center third cycle and its original-time clock stay fixed in the same quartic family, with an explicit leading determinant. The family, hyperbolicity criterion and parameter-independence of the third angular speed already follow from Cao–Llibre. No inspected prior statement yields the simultaneous fixed-degree, fixed-geometry rank assertion.

## value

PASS

The result identifies a concrete separation of dynamical controls in a minimum-size explicit circle family: two least-positive periods can be varied independently without moving even the off-center cycle or changing its clock or the degree. Universal nondegeneracy across admissible nested and exterior geometries, rather than one lucky parameter choice, makes it a useful complement to general period realization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
