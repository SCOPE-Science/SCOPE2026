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

Every maximal geodesic in K_{n,n} minus a perfect matching is a length-three path a_i-b_j-a_k-b_i with pairwise distinct i,j,k. Omitted-index criterion U=empty OR |R|=1 OR |C|=1 OR R=C={i,h} is an exhaustive equivalence. Counting these sets by inclusion-exclusion yields T_n, removing chosen vertices classifies the three disjoint minimal families and M_n, and the explicit p=floor(n/2) vertex-disjoint length-three paths attain the vertex-count packing bound. Recomputed independent BFS maximal-path hitting sets for n=4,5,6 (24,60,120 maximal geodesics) and all 2^(2n) subsets; T_n and M_n agree exactly. This is finite corroboration of the unlimited-n combinatorial proof.

## originality

PASS

Best-of-knowledge original exact transversal and inclusion-minimal cardinality polynomials and packing ratio for crown graphs. The highly similar crown geodetic-set polynomial is an inequivalent coverage convention: it seeks S whose intervals cover all vertices, while this theorem hits every maximal shortest path. Earlier geodesic-transversal and packing papers establish the parameters and some other graph classes without the three-family crown enumeration. Full historical journal texts were not all accessible.

## value

PASS

Natural vertex-transversal versus disjoint-geodesic-packing invariants on a highly symmetric matching-deleted complete bipartite graph. The exact minimal-set spectrum and unbounded gaps are structural, the polynomial enumerates every irredundant configuration, and the exact packing ratio answers a natural covering/packing comparison beyond a small finite tally.

The dated certificate retains the supplied scientific assessment, sources and limitations.
