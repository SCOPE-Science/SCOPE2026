---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The 9! labelled permutations were exhaustively filtered into 133496 derangements, legal swaps examined at all 36 pairs of positions, and shortest-path BFS recomputed for eight representatives of all conjugacy classes. Independently written C++ produced graph degree sum 3671136, all eight eccentricities (9,8,9,8,10,9,8,8), and one inverse antipode at distance ten in the (3,3,3) class, no others. Conjugation equivariance proves class exhaustiveness; 2240 such derangements yield 1120 unordered inverse pairs. The BFS certifies only n=9, not an unbounded diameter theorem.

## originality

PASS

Earlier inverse-three-cycle theorem already establishes the particular k=3 inverse-pair distance ten but does not prove global diameter, the uniqueness of all diametral pairs, the full eccentricity table, or the count 1120. Dyer–Jerrum–Müller address switch mixing/graph families; Jain handles degree/connectivity. The new exact metric census therefore survives on best-of-knowledge comparison.

## value

PASS

First complete exact eccentricity distribution and rigidity of diametral pairs for an intrinsically natural 133496-state perfect-matching switch graph, with meaningful optimal geodesic constraints and checkable finite certificate beyond textbook degree/inclusion-exclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
