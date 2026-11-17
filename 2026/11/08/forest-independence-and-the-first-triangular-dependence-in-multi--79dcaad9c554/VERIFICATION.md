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

PASS: For each index-graph edge (i,j), the relative permutation Q_ij=pi_i^{-1}pi_j classifies the isomorphism type of the pair of directed successor paths, so all pair-local FO² truth tests depend only on Q_ij. For a forest, root labels together with independent edge differences form a bijective coordinate system of k independently uniform permutations. On a cycle, equality-of-successor sentences have joint probability (n!)^{-(k-c(G))} versus product (n!)^{-|E(G)|}, proving the iff. For quantitative overlaps, an ordered edge is present with probability 1/n; two distinct compatible edges with probability 1/[n(n-1)]. The exact triple sum over directed edges yields raw moment (n^4-4n^3+8n^2-8n+1)/[n²(n-1)²] and centered third cumulant (n^4-2n^3+2n²-4n+1)/[n³(n-1)²], positive even for n=2. Independent full enumeration of 2!,3!,4! order triples reproduced cumulants 1/8,17/54,145/576 exactly. These finite tests support the all-n enumeration and forest-coordinate proof.

## originality

PASS

PASS best-of-knowledge: generic group differences on a forest are a known mechanism and not separately claimed new; the pair-local logical characterization and exact n-dependent triangle mixed third cumulant of random successor-path overlaps remain uncovered by the inspected two-order adjacency marginal and other same-pattern results.

## value

PASS

PASS: Exact universal graph-indexed independence for any pair-local logical events, together with the natural first nonzero triangular third cumulant of shared directed adjacencies, distinguishes pairwise independence from higher-order dependence in multiple-successor random structures. Group-edge independence is classical and credited, but the explicit path-overlap cumulant is a meaningful model-specific statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
