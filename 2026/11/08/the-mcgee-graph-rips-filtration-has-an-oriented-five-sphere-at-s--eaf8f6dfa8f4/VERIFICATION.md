---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run \(\texttt{python3 mcgee_rips_verify.py}\) with Python 3 and no third-party packages. The standalone verifier generates the precise LCF graph, independently computes all-pairs shortest-path distances, confirms 24 vertices, 36 edges, girth seven, and pairwise distance counts \((36,72,144,24)\). It inductively enumerates every face of the scale-two Rips clique complex, checks the vector \((24,108,96,24)\), and verifies 96 relative elementary-collapse pairs in each of two opposite selection orders, with exactly the original graph remaining.

It then verifies that all 24 pairs at distance four form six disjoint four-cycles, checks all their bipartition pairs and the 64 facets of the scale-three complex, and uses the exact polynomial \((1+4t+2t^2)^6\) for the total of 117649 faces including the empty face. It enumerates 32 graph automorphisms by complete adjacency-preserving backtracking, checks the orientation sign for each, and verifies 16 of each sign, including a negative sign for rotation by three.

The executable output is embedded verbatim as \(\texttt{mcgee_rips_verification_output.json}\). These finite checks establish the identities used in the mathematical join and CW-collapse proof; they do not constitute an independent audit or establish any general result for all cubic graphs.
