---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

In a selected K_r clique plus n independent leaves, the longest simple (not necessarily induced) path on p clique and q leaf vertices has order min(p+q,2p+1): leaves must be separated by clique vertices, and alternating with adjacent clique insertions achieves the bound. Thus the t-path-free faces satisfy min(p+q,2p+1)<t for r,n>=2,t>=5. The closed star at a chosen leaf v is a cone, and its complementary simplices are exactly size t−1 and p>=ceil((t−1)/2), with boundaries entirely in the star. The quotient is a wedge of B(r,n,t) spheres S^{t−2}; the relative integral oriented facet chains yield the S_r×S_{n−1} exterior-power direct sum. For S_r×S_n the augmented Hopf trace on invariant faces and cycle-polynomial weights gives the stated rational character, and each p>=2 wedge exterior power has no S_r invariant via a transposition of two selected clique labels. Independent separate graph-DFS enumeration and mod-two chain ranks agree for four small (r,n,t) triples; that does not prove the quantified integral statement. Edge cases t>r+n and B=0 are covered by the cone.

## originality

PASS

Best-of-knowledge PASS with specifically described primary-source, broader-implication and alias comparisons; unindexed equivalents and two inaccessible highly relevant full texts remain real residual risks, not falsely declared excluded.

## value

PASS

All path lengths t>=5 across natural complete split graphs receive an exact integral homotopy classification plus an explicit integral stabilizer module and full group cycle-type character. The latter symmetry data and vanishing invariant lattice are not determined by the wedge multiplicity, making the result useful to equivariant graph-complex topology, beyond routine parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
