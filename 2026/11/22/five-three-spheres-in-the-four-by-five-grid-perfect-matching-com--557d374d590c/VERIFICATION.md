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

Enumerating perfect matchings by assignment of black vertices to distinct adjacent white vertices and taking all nonempty edge submasks gives exactly 95 facets and 50,462 faces. An independent acyclic matching with 25,228 pairs leaves one critical vertex and five critical three-cells; its complete reversed Hasse graph topologically sorts all 50,462 faces across 289,078 incidences. Forman's CW reduction therefore gives five 3-cells attached to a point. This also avoids reliance on any numerical rank or on the frozen matching's tie order. The latter certificate was separately reconstructed, including critical counts (1,1,6) in dimensions (0,2,3) and the exact signed Morse row (1,0,−1,−1,0,0). Its unit attachment makes the two-sphere plus that three-cell a contractible CW subcomplex, which can be collapsed up to homotopy. Each perfect matching has ten edges, hence the complex is pure of dimension nine; nonzero reduced homology below dimension nine excludes pure shellability.

## originality

PASS

The substantive claim is the integral homotopy type for the open P4 × P5 perfect-matching extendibility complex. The strongest inspected grid theorems concern widths two and three, and the close indexed computations change either the dimension, the periodicity or the complex. None of those changes preserves the claimed face poset or supplies the asserted integral type.

## value

PASS

Tests the open rectangular sphere-wedge conjecture at a natural larger width with an odd second side, gives the exact integral sphere multiplicity and degree, and distinguishes the perfect-matching subcomplex from both the ordinary matching complex on the same graph and the mixed-dimensional 4×4 case. The non-shellable pure example and exact homotopy type are useful checks on potential four-row formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
