---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Every triple of normals is independent. Orient the uniquely dependent four-tuple so its coefficients are positive. A strict sign chamber is impossible exactly when its signed normals have a nonzero nonnegative dependence, hence exactly the two constant signs are excluded. A singleton-sign constraint follows from the other three. In a two-two chamber every hyperplane is a facet: feasible witnesses for opposite signs of that coordinate can be joined, keeping the other three inequalities strict. Thus the eight triangles and six quadrilaterals meet along edges always of mixed type, so triangular perimeters total 8π and the minimum is at most π. If the minimum equals π all triangles have perimeter π; polarity gives four normal-triple areas of π. The solid-angle formula has positive determinant magnitude and returns area π precisely when 1 plus the three pairwise dots vanishes. Subtracting the four equations yields equal opposite-pair Gram entries and the sum −1. The Gram matrix is realized by the stated sign pattern with positive a,b,c and squares summing to one; congruence is orthogonal since each triple spans. Conversely this Gram condition makes all triangles have perimeter π. The polar of the ++−− chamber is the radial rectangle at x=a. Integrating (1+s²+t²)^(-3/2) over the rectangle uses the mixed primitive arctan(st/sqrt(1+s²+t²)); its area is 4 arctan(bc/a) after unit normalization. Cyclic permutations and antipodal symmetry give all quadrilateral perimeters. Monotonicity of arctan gives exactly the three non-strict constraints. The regular point satisfies them strictly, and the unordered (a,b,c) are determined by the normal Gram data up to permutation, so a two-dimensional family survives modulo isometry. The boundary, including an additional quadrilateral of perimeter π, is allowed.

## originality

PASS

Best-of-knowledge pass for the complete nonrigid optimizing region and its exact quadrilateral profile for the geodesic perimeter objective. Credit established incidence and polar/solid-angle methods. The π upper bound is short once the incidence sum is known; that observation is not the sole novel contribution.

## value

PASS

A natural extremal question for the first four-circle arrangement with two cell types has an explicit, exhaustive equality set. Nonrigidity distinguishes perimeter optimization from nearby rigid area problems, and the quadrilateral formulas give an exact membership test including boundary cases. This is substantive beyond the incidence-average proof of the bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
