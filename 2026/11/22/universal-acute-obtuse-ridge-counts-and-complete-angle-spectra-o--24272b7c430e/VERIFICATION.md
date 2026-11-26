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

The feasible part masses t_i lie in the rank-two hypersimplex; choosing an edge between a pair of parts with those pair marginals and choosing its endpoints from the normalized within-part weights recovers the given feasible vector. Strict feasibility uses t_i=2/k distributed positively within each part; the frozen proof's stray suggestion x_v=2/n is not valid for unbalanced sizes, but its immediately following strictly feasible construction is. After deletion of one or two vertices every part survives, so coordinate facets and their pair intersections have the stated dimensions, by the same strict feasibility in remaining coordinates. A part-cap face is a product of two simplices, and one coordinate deletion lowers its dimension by one; two caps force all mass into those parts, dropping dimension to at most n−5. Each ridge belongs to exactly two facets (its pointed two-dimensional normal cone). Within the sum-zero direction space, c_v=−e_v+1/n and d_i=1_{A_i}−a_i/n (constant vectors implicit) give squared norms (n−1)/n and a_i(n−a_i)/n. The coordinate cross term is −1/n and the coordinate–cap cross terms are −(n−a_i)/n inside and a_i/n outside. Taking the supplement of the projected normal angle gives precisely both signs, the multiplicities and the split adjacency graph. The two cap families are strictly increasing in a_i at fixed n and lie on opposite sides of π/2; equality of the acute cap angle with the coordinate angle requires a_i=n−1, excluded here. An independent rational affine-rank and signed Gram test passed profiles (3,3,3), (3,3,4), (3,4,5) and (3,3,3,3).

## originality

PASS

Credit the known face structure and f-vector of these rank-two matroid polytopes. Pass the complete intrinsic ridge-angle spectrum and the uniform acute/obtuse census despite variation of the exact spectrum. The closest earlier angular match uses a different statistic on the same object, and the closest earlier ridge-angle match uses a different polytope. The exact angle classes do not follow from the known face counts; the analysis distinguishes facet normals by their part-incidence signs and normalized magnitudes.

## value

PASS

The full interior dihedral spectrum is a natural intrinsic metric invariant of canonical rank-two base polytopes, not merely the f-vector in different notation. Its exact classification distinguishes uniformity of the coarse acute/obtuse data from monotone dependence on class sizes of every genuinely metric cap-angle family. The full multiplicities and noncollision property matter for comparing the Euclidean geometry of polytopes with the same facet-adjacency graph; the value does not rest on the already-known number of ridges or on any single routine angle computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
