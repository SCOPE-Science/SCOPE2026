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

Generic normal-vector support maximizes by assigning the k largest positive coefficients the labels n,n-1,...,n-k+1. Adjacent coefficient switches exchange consecutive labels, length sqrt(2); a coefficient crossing zero inserts/deletes the smallest positive label, length n-k=d+m-k. Their multiplicities are A=((m-2)N+2)/2 and B_j=m!/(j-1)! for j=1..m. Exact combinatorics sum to mN/2 edges and total insertion length m![(d+1)E_(m-1)+E_(m-2)]. Since N~e*m!, substitution gives insertion-length share 2c/(sqrt(2)+2c) for d/m->c (including 0,infinity) and the fixed-d refinement; B_j/(N-1) is the shifted truncated Poisson(1) law, and length-bias decomposes as mixture of 1+Y and 2+Y. Separately recomputed exact factorial edge counts and insertion length sums for m=2..8 with d=0,1,m,2m; those computations only corroborate all-parameter normal-fan proof.

## originality

PASS

Behrend et al Proposition 5.7 characterizes the very same two classes of edges for anti-blocking permutohedra, and Corollary 5.8/Remark 5.9 explicitly transfer them to partial permutohedra: the original combinatorial edge classification is covered. The audited statement, however, counts edges at each actual Euclidean length and derives an exact Poisson insertion-edge spectrum and count-versus-total-length transition as dimension and label surplus co-grow. The inspected published face-lattice/volume/Ehrhart results do not give these metric-weighted limits. Comparison to published mean-width and covariance results also concerns different integrals over directions/vertices.

## value

PASS

The one-skeleton Euclidean length distribution is a canonical geometric invariant of a natural polytope family, and length-bias reveals a concrete qualitative transition invisible to the known m-regular edge count. A vanishing 2/m fraction of edges controls nonzero asymptotic fraction of metric length when surplus d is linear in m, with a precise shifted-Poisson local spectrum. This is a motivated full exact classification, despite relatively elementary factorial arithmetic once adjacency is known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
