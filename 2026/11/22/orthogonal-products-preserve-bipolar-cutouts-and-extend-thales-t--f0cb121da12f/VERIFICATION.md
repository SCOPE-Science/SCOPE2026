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

A product facet is a facet in exactly one factor times the other whole factors, giving O1. South and north faces and their nonempty intersections separate coordinatewise, giving O2 in both directions. To test the vertex order using all north faces one can hold the other factor faces whole, so the order is precisely the product order. An atom changes one coordinate from its bottom element, and the south interval has directions only in that factor. Its north interval has the corresponding factor north directions plus all other factor directions, hence O3 holds by factor perpendicularity and the orthogonal embedding. Relative interiors, projections and normal cones separate coordinatewise. Convex hulls of Cartesian products factor, for example by multiplying factor convex-combination weights, yielding the cutout identity even off the kernel. For dimensions two and three the inspected Thales result supplies bipolarity and the normal-cell identity under kernel membership. The source leaves the one-dimensional case implicit: an interval is cut into its two subintervals at B, each with O1 and O2 immediate and O3 vacuous since one interval direction is zero; the two halves are exactly the normal-cone restrictions. The cells cover by maximization at some vertex, and two distinct cells meet precisely on their common support-score tie hyperplane (if nonempty), a face of both. Arbitrary triangle shapes are allowed because an incenter projects to the interior of each side; this does not say that an arbitrary interior anchor in each triangle is valid.

## originality

PASS

The metric product rule for the bipolar configurations, joined to the exact factorization of the actual cutouts, provides a distinct higher-dimensional family for the open implication. The low-dimensional factor tiling theorem and generic fan tiling are verified prior inputs, and coordinate projection identities and abstract product lattice identities are not claimed as standalone novelties.

## value

PASS

This gives a reusable metric closure principle on actual Euclidean realizations, and lifts a dimension-limited theorem to a broad higher-dimensional decomposable class containing non-box and non-simplex examples. The natural question is equality of the projection cutouts with the fan cells, not whether a Cartesian fan can be written down. The result also allows an admissible anchor test factor by factor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
