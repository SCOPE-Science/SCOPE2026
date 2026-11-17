---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The Munn tree is a subtree of the free-group Cayley tree. For endpoints u,v the minimum complete-tree visiting walk is exactly 2E-d(u,v), by parity of each tree edge cut and a matching Euler walk. The published Green-class root constraints give D/R/L minima 2E-diameter, 2E-eccentricity(root), and 2E-eccentricity(terminal). Fixed-rank free-group prefix equality is deterministic logspace by classical modular-matrix method. Scanning first occurrences counts distinct prefix vertices with O(log n) counters. For each segment, count first-occurrence undirected edges with odd traversal parity; exactly these lie on the path between segment endpoints. Each equality and distance calculation uses O(log n) work bits and polynomially many rescans, so maxima and three tests use deterministic logspace. Empty word and rank-one cases are covered; no claim of uniform input alphabet.

## originality

PASS

The 2026 Bodart–Carvalho–Monteiro primary paper provides Munn-tree characterizations and asks whether Green-geodesic languages are context-sensitive, not deterministic logspace. The October 18 linear-space algorithm already implies context-sensitive membership; it does NOT give O(log n) workspace. A separate conjugacy-geodesic logspace result addresses different equivalence classes, not Green D/R/L. The parity-edge counting reduction is the specific new improvement, despite synthesis of standard algorithms.

## value

PASS

A logarithmic-space upper bound strictly improves a known deterministic linear-space bound for three natural semigroup representative languages and answers a published classification problem at an unexpectedly low space level. The crossing-parity implicit tree algorithm is mathematically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
