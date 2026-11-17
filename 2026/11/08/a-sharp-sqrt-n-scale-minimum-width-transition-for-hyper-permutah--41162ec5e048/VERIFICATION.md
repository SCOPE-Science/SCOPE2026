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

PASS: Minkowski support-range additivity counts mixed k-hyperedges across a centered cut as C(s)=binom(n,k)−binom(s,k)−binom(n−s,k). Every sorted zero-sum direction is a nonnegative linear combination of nested centered indicators, with exact support-range additivity and Euclidean triangle inequality, yielding global minimum over cuts and strict equality only for a single positive coordinate gap (all two-level normal ties included). For k_n/sqrt(n)→c>0, fixed-size cuts have normalized limit c sqrt(s), macroscopic cuts ≥2 with equality only balanced, and intermediate-size cuts diverge, proving min(c,2) and strict eventual singleton/balanced minimizing types off c=2. Independent n=3..8 hyperedge count/support evaluation corroborated finite formula.

## originality

PASS

PASS best-of-knowledge: The hyper-permutahedron and its combinatorics are known; the Euclidean mixed-hyperedge minimum-width structural theorem and k~sqrt(n) sharp phase do not follow from inspected polytope face enumeration or distinct hypersimplex width results.

## value

PASS

PASS: Exact Euclidean minimum width of a natural all-k-uniform hypergraphic Minkowski sum, complete minimizer classification and sharp sqrt(n) scale threshold give a usable intrinsic geometric invariant not inferred from known face-enumeration tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
