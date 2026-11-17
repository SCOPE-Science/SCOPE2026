---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The ordinary matching complex is formed from every set of pairwise disjoint edges in GP(12,5), not only perfect-matchable subsets. Independently generated the entire matching-count polynomial (1,36,558,4884,26613,93888,216228,320256,293436,155024,41832,4608,120), total 1,157,484 augmented faces. Source C++ explicitly builds all matchings, pairs along indexed edges, topologically sorts all 8,344,008 augmented Hasse arrows, and eliminates signed 7-to-8 incidence pairs. Its critical cells are one 0, 132 in dimension 7, 40 in 8. Independently loaded its actual 132×40 Morse boundary matrix via GitHub blob and performed exact unimodular unit-pivot row/column operations: 34 pivots of ±1, remaining block all zero, proving its Smith factors (1×34,0×6), no torsion. The 7-skeleton is ∨132 S7, so the integral degrees classify all 8-cell attaching maps; 34 cell pairs cancel to yield 98 S7 and 6 S8.

## originality

PASS

Best-of-knowledge no prior matching coverage for this exact integral homotopy statement; compared same and broader objects.

## value

PASS

The ordinary edge-matching complex of the symmetric Nauru GP(12,5) graph is a canonical graph complex. Determining both integral 98 and 6 sphere multiplicities in two adjacent high dimensions, and excluding torsion, supplies a natural missing exact invariant that the earlier perfect-matching and vertex-independence calculations do not determine. It is a useful benchmark for future generalized-Petersen or graph-matching classification and for testing Morse methods, without requiring a universal theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
