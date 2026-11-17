---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The scalar Kalman inverse update yields u_n=1/P_n-1/(sP_(n-1)+q) and a telescoping precision-g(P) balance with uniformly O(1) endpoints. The reachable-domain g=1/p-1/(sp+q) is strictly decreasing and convex for s>=1, and eventually for s<1; Jensen gives lower liminf p_b for any Cesàro schedule with b>0. Constant u=b converges to p_b. Positive increasing concave periodic Riccati map has a unique attracting periodic orbit, and strict Jensen equality forces all P_i and u_i equal. Independent periodic numeric checks support, not substitute for, the infinite proof.

## originality

PASS

The fixed Cesàro-mean divisible observation-precision optimization for long-run scalar posterior variance and unique periodic constant allocation differ from finite-horizon discrete measurement placement, periodic precision under an error upper bound, and general discrete sensor scheduling. The information-balance Jensen proof delivers an exact all-stable/unstable frontier. An older unindexed scalar precision-allocation theorem remains possible.

## value

PASS

The choice between smooth and intermittent sensing is a natural precision-budget control problem. The theorem supplies the exact every-Cesàro-schedule lower bound and unique fixed-period optimizer even for unstable scalar systems, distinguishing divisible precision cost from discrete sensor count. It is a complete justified classification for its model, not merely a rephrased Jensen inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
