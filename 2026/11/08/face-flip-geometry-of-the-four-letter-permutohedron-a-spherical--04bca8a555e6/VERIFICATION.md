---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

A 24-vertex S4 Cayley graph with three adjacent-transposition generators has 36 edges and exactly 14 facial cycles (six squares, eight hexagons). Recursive least-uncovered-vertex enumeration lists all 169 perfect matchings; a facial XOR mask gives all legal flips. Complete BFS from each of 169 matchings yields a connected all-face graph with 460 edges, radius 7, diameter 9, exact eccentricity and distance distributions. All 790244 unordered matching triples were tested by intersecting three exact shortest-path intervals: 79828 none, 700774 one, 9642 two medians. Omitting each of the 14 faces gives connected plane flip graphs, with square omission 410 edges/radius 11/diameter 22, hexagon 440/11/21; two geometric enumerations and an additional independent implementation confirm values. This is exhaustive finite graph certification, not extrapolation.

## originality

PASS

PASS best of knowledge: Strunje 1986 already counted the 169 perfect matchings; 2026 Wang–Kang and earlier plane resonance lattice theory establish qualitative medianity of proper face subsets. But the exact 460-edge all-face metric, all 14 quantitative deletion spectra and concrete nonmedian triple are not implied by these general theorems or by prior matching census. Historical overlap possible in inaccessible Lam–Zhang 2003 and unindexed computational tables.

## value

PASS

PASS: A natural minimal nontrivial three-dimensional permutohedron yields an exact striking metric contrast: permitting its spherical outer-face flip decreases diameter 21/22 to 9 but destroys medianity. Complete graph-geometric invariants and the canonical generator triple are independently useful, not arbitrary tiny numerical slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
