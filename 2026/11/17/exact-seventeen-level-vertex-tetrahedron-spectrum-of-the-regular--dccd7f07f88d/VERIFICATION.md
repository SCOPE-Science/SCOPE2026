---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The truncated octahedron is [-2,2]^3 intersect sum|xi|<=3 with exactly 24 integer vertices and volume 32. All vertices have odd coordinate sum, so three-edge determinants are even. Independently enumerated all combinations of 24 signed (0,1,2) vertices with integer 3x3 determinant, obtained the complete exact table 846,552,1728,1152,1332,456,1872,360,654,408,480,72,468,48,144,24,30 at even determinants 0..32, sum 10626. The package code supplies a separate full 48-element signed-permutation orbit partition (265 orbits, max size-6+24) and the 4D permutahedron perfect-square Gram cross-check; code read/checked for algorithmic completeness, orbit partition not independently executed this turn. Squared edge-distance six-tuples separate top two congruence classes. This is exhaustively finite: no infinite theorem extrapolated.

## originality

PASS

The published cube–octahedron intersection family exactly determines the maximal inscribed tetrahedron volume 16/3 and occupancy fraction 1/6 here, so those are explicitly NOT original. It leaves all optimizer classifications and lower frequency levels unresolved; the complete 17-level 10,626-case frequency table, maximum orbit decomposition and vertex-restricted second gap are not implications of its maximum-only bound.

## value

PASS

An exact natural finite invariant of a canonical Archimedean cell, the full tetrahedron volume spectrum and orbit-type classification is useful in polytope geometry, lattice discretization and tetrahedral mesh comparisons. The 17-level, top-orbit and discrete gap features are nontrivial structural data, not an arbitrary slice or known maximum recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
