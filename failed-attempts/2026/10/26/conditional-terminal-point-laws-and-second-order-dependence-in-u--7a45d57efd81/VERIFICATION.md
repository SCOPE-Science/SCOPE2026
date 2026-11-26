---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For fixed cyclic set S of size k, deleting the cycle edges leaves an independent uniform S-rooted forest. The nonroot matrix-tree minor nI−J has determinant k n^(s−1), s=n−k≥1. Removing r prescribed nonroots with no children and reattaching them to the n−r survivors gives k(n−r)^(s−1) forests, including r=s with k^s attachments. The prescribed-set probability at RESULT line 80 is naturally read conditional on the fixed S, as in the preceding construction; without that conditioning a fixed set A can contain cyclic vertices. The factorial-moment sum is over the s nonroots for each S, giving exactly the claimed law conditional on C_n=k, and separately Z_n=0 at k=n. The mean f(s)=s(1−1/n)^(s−1) increases strictly up to feasible s=n−1; the strict negative sign follows by the independent-copy covariance identity. Deleting a specified terminal leaves a uniform map on n−1 vertices and the cyclic count unchanged, which gives the exact covariance identity after summing over terminals. The cycle mass telescopes to survival (n)_k/n^k and yields b_n as the mean. The log expansion cancels the linear-in-k terms and gives n/e+(1−k²/n)/(2e)+o(1) uniformly to n^(3/5); the cycle survival bound handles the complement and gives Rayleigh moment convergence. Then Cov(R,R²)=sqrt(π/2) gives the mixed limit, and empty-bin pair indicators give Var(Z_n)/n→e^(−1)−2e^(−2) and the correlation constant. These arguments cover n=2 and the degenerate k=n forest.

## originality

FAIL

An earlier distinct indexed record gives the same conditional factorial moments, strict regression and negative sign, covariance and correlation limits, and the same second-order mean expansion in its proof. The finite b-difference identity is a direct consequence of its exact conditional mean and cyclic marginal, and is explicitly stated in another indexed refinement. No substantial distinct part survives these statement-level comparisons. Relative catalog dates distinguish the sources but do not establish broader historical priority.

## value

FAIL

The exact mixed dependence and second-order cancellation would be valuable for the natural uniform-map model if distinct. The earlier indexed result gives the same phenomenon and constants with a uniform mean expansion, and the finite identity is already determined by its exact formulas. The terminal-deletion proof is neat but adds no distinct exact information or new applicability regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
