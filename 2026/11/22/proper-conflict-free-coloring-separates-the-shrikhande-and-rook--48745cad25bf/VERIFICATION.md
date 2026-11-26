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

The independently recreated graphs each have 16 vertices, 48 edges, degree 6 and exactly two common neighbors at each pair of distinct vertices. For an independent class C of size t, counting its incidences and shared neighbors gives Σa_x=6t and Σa_x²=2t(t+2). Cauchy–Schwarz gives t²+4t−32≤0 and hence t≤4, with a_x=2 at every outside vertex when t=4. Four colors would force four maximum classes and multiplicities 2,2,2 in each open neighborhood, precluding a singleton. For the rook graph with five available colors each row and column omits exactly one. The multiplicity of any missing color is the same among rows and columns, because its occurrences lie in distinct rows and distinct columns. Choose a row and column with the same missing color; at the intersection the two palettes after dropping the center color coincide, so every encountered color occurs twice. Thus five colors also fail for the rook graph. Both supplied arrays were validated by independent code under the exact Cayley-step and row/column definitions: all edges proper and all 16 open neighborhoods have at least one singleton in each array. The asserted values 5 and 6 follow.

## originality

PASS

The claimed distinct contribution is the Shrikhande value and separation of the parameter twins. The rook value is explicitly credited and is exactly covered by the dated rectangular/square rook theorem. No inspected Shrikhande exact statement or dominating theorem gave the five-color proper open-neighborhood conflict-free value.

## value

PASS

The Shrikhande and rook graphs form a canonical same-parameter and cospectral pair. The exact values give a concrete counterexample to determining proper open-neighborhood conflict-free chromatic number from either that parameter set or the spectrum. A sharp certificate plus parameter-based common lower bound distinguishes the S value from an arbitrary computed graph statistic; the credited rook value makes the contrast precise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
