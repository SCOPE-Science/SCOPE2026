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

The stated mathematical modulus holds. In hub-relative coordinates d, the dual solves a box-constrained strictly convex QP with Hessian G=diag(1/m_i)+11^T/m_0 and output edges d-Gp. On a strict fused set S the free dual variables yield differential h_j-sum_{i in S}m_i h_i/(m_0+sum_{i in S}m_i) for j outside S, and zero in S. The exact weighted column sums are bounded by the singleton-fused columns and by 1 for the unfused columns. All patterns are realized with interior dual values on fused spokes and nonzero gaps on other spokes; the finite affine decomposition gives the upper bound on entire segments, by continuity also on boundaries. k=1 is included. At unit masses, unit weights and unit penalties, x=(-3,0,2,2,2) and x+epsilon e_1 for epsilon=1/5 give a ratio of 3/2 by exact KKT. The independent replay is `python3 -B /workspace/review_replay.py`, check 5. Source RESULT.md line 71 has corrupted LaTeX alpha tokens (U+0007); the single-input inequality it means is nonincrease of regularizing TV by comparison with u=x. No uploaded checker was executed.

## originality

FAIL

Earlier indexed work already covers the same exact invariant by a direct active-block equivalence. The weighted rooted-star isotonic result states the sharp two-input edge-variation amplification over weighted isotonic least squares (including the choice of positive measurement edge weights). For constraints u_i>=u_0, its strict pooling regions have exactly the same linear parts as the present star TV map. In particular every S occurs in isotonic regression: choose u_i=u_0 on S, u_j>u_0 off S, and positive inequality multipliers on S, then define x from the weighted KKT equations. Its differential is mass averaging on {0} union S and identity elsewhere. Thus the entire set of induced edge-variation norms, its maximum, and the maximizing coordinate perturbation transfer unchanged to the TV map for each positive penalty vector. This is concrete prior coverage of the coefficient and thresholds, not rejection for a missing full text. The separately indexed earlier general graph-TV modulus already describes exactly this connected-block maximization and penalty independence; its precise independent-weight hypotheses could not be confirmed, so it is corroborating evidence, not the sole basis for failure.

## value

FAIL

The norm and its branching threshold are natural and useful. However, the value proposed as a new exact invariant is already obtained from the earlier sharp edge-variation analysis of the same mass-averaging face family. The penalty independence is also in the earlier graph-TV statement. Rewriting the same column norms for TV and specializing the parameters does not leave a separately valuable unknown result under the exact-invariant standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
