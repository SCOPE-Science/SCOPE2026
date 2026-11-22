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

For the unfilled cycles C_m,C_n (m,n>=4) each tetrahedron of their join consists of two edges, one per factor. All three opposite-edge pair partitions in each tetrahedron form exactly K_{m,n} between same-factor edges and the categorical product C_m x C_n between cross edges; there are m+n+mn double vertices, 3mn edges, and no mixed adjacencies or higher faces. The product is 4-regular with mn vertices and 2mn edges, connected iff at least one cycle is odd; if both even it splits by bipartite parity into exactly two equal components. Spanning-tree contraction gives K Betti (m-1)(n-1), product Betti mn+1 or two of mn/2+1, torsion-free integral H_1 and no higher homology. Under factor-preserving D_m x D_n, K vertices have two orbits and edges one orbit -> interval; product vertices and edges each one orbit, but a reflection reverses an edge, so its actual geometric quotient is a half-edge interval, not a loop. Together the quotient is two disjoint closed intervals. Inspected verify.py direct facet enumerator for 49 ordered small cases; bounded examples matched 4x5 and 6x8, and symbolic facet argument handles all m,n.

## originality

PASS

PASS on best-knowledge statement/implication comparison, NOT a proof of absolute literature priority. Prior and current result evaluated using actual source theorem and full relevant published primary work; residual risks specifically documented.

## value

PASS

A transparent all-parameter structural classification shows simplicial double of a three-sphere can have disconnected large first homology while the true finite-group geometric quotient has only two contractible components. The parity-driven topology and edge-inversion subtlety are meaningful counterexamples/boundary descriptions for doubling and equivariant topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
