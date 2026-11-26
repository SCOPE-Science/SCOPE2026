---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The sandwich idempotence equation bounds rank by two. Rank-two idempotents take the two sandwich image labels to a pair of points in the corresponding two disjoint fibers, and independently choose either value on the other n-2 inputs. Distinct constants cannot commute; a constant commutes with a rank-two idempotent exactly at one of its two image points. If two rank-two idempotents commute, equality of product images first identifies their two output points, in the unique fiber order; then the products are the two original maps in opposite order, forcing equality. This establishes subdivision with t copies for every edge. In the unsigned incidence Gram matrix the two within-fiber sum-zero blocks contribute vt and ut; the 2-by-2 quotient contributes nt and 0. The signed pairs of square roots and rank give the stated polynomial even for n=2 or singleton fibers. The spectral radius and graph order recover n and uv. For n>=4 degree separation and the common-neighbor relation recover the base biclique; each fiber of twins can be permuted independently and base automorphisms lift. Independently enumerated all 104 rank-two sandwich maps on n=2,3,4 via /workspace/branches/reproduce_sandwich_independent.py, checking neighbor sets and exact characteristic polynomials. Read the frozen checker and recorded output without running them; the unrestricted result follows from the proof. A checker comment about degree-two vertices must be read with the n>=4 scope of the statement.

## originality

FAIL

The strongest distinct same-day match contains more than an aggregate count: its proof gives the complete labeled boundary types and the exact pointwise criterion for every rank-two-variant commuting pair. Restriction to the known idempotent parameterization yields exactly the claimed graph; the spectrum and automorphisms then follow from standard incidence diagonalization and the twin classes. This establishes coverage by an available broader formulation, not that the same-day article necessarily came first. Its relationship passage in fact refers to an earlier idempotent-commuting-graph result, without a distinct source ID for that reference.

## value

FAIL

The graph is a natural invariant and the recognition result is correct, but on the evidence here the graph is a direct specialization of the complete broader criterion. The remaining formulas use only standard incidence-block spectra and twin permutations, and recover an existing kernel invariant. No separately valuable non-mechanical claim remains within the frozen scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
