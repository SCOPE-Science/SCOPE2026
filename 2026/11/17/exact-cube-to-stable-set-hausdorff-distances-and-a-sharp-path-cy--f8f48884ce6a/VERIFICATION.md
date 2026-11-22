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

The stable-set polytope is coordinatewise downward closed, so projection of all-ones dominates every cube point; its projection coordinates are all strictly below one for paths/cycles, giving unique farthest point. Cauchy–Schwarz and maximum independent set orbit mixing yield the general graph bound with exact equality condition. For paths, edge constraints form the integral stable-set hull (bipartite TU); displayed positive KKT multipliers and sum-of-squares identity give the unique minimizer in every order including n=2. Cycles use vertex transitivity and alpha=floor(n/2), giving exact squared gaps and the even-zero, odd-(n+1)/(2n) edge-closing jump. Reconstructed exact path KKT stationarity for n=6,7,8,9; all pass. Finite checks support but are not the universal proof.

## originality

PASS

Best-of-knowledge noncoverage after implication comparison; Prior geometrical/combinatorial graph polytope statements do not by implication determine the exact ambient Euclidean cube gap or parity jump.

## value

PASS

The complete exact Euclidean Hausdorff metric of two central graph-polytope families, the sharp general equality criterion and a parity-sensitive single-edge stability law are motivated quantitative convex-combinatorial invariants. A classical polytope description alone does not fix the nonlinear Euclidean projection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
