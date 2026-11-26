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

I independently reconstructed all concurrent line triples using 3-by-3 determinants in Z[a]/(a^2+a+2), then assembled the maximal incidence sets. They give precisely 28 triples and 21 quadruples, four of each type on each line. Blowing up separates distinct tangent directions at each multiple point; every exceptional-line intersection is a node and strict lines are disjoint. The connected graph has 70 rational-component vertices, 168 edges and first Betti number 99; every valence is at least three. I recomputed the quadruple-adjacency characteristic polynomial and a full Laplacian minor determinant by exact elimination, obtaining 2^26 3^23 7^5 719^6. Independent prime-power elimination on the 69-by-69 minor gave 60 unit factors followed by 4, 72, 216, 155304 and five factors 1087128. The shipped local step can use row clearing only: after clearing the column below a minimal-valuation pivot, clearing its row by column shears leaves the trailing block unchanged. The Schur determinant separately follows by weights 4 for triple adjacencies and 3 for quadruple adjacencies. In the specified regular semistable unit-thickness setting the graph is already the one used by Raynaud's theorem, so the same critical group describes the geometric Néron component group.

## originality

PASS

Best of current knowledge, the distinct supported contribution is the exact integral group of the full 21-line/49-point incidence boundary. The arrangement, this ambient blowup, and the graph component-group theorem are not new. The same-day exact subgraph computations are genuine related claims but neither contains the integral calculation for the full graph. The identical mirrored record is not independent evidence of earlier coverage.

## value

PASS

The graph comes from the canonical complete normal-crossings resolution of the classical Klein arrangement, not an arbitrary graph slice. Its invariant factors identify exactly the component group of a unit-thickness smoothing and distinguish cyclic structure that genus and determinant alone do not. The six 719-primary factors are genuinely new information relative to the two point-type-only computations and relevant to integral degenerations with this central fiber.

The dated certificate retains the supplied scientific assessment, sources and limitations.
