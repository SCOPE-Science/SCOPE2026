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

The analytic verification uses the exact AR(1) two-site conditional covariance, a uniform Taylor expansion valid whenever \(n(1-\rho_n^2)\to0\), and strict convexity of the limiting two-site objective. These jointly prove the asymptotic ratios; no finite computation is used to infer an infinite-dimensional statement.

Run `python check.py` to reproduce the independent exact-rational comparisons of finite Schur complements and the greedy farthest-endpoint restriction. The program also prints floating-point asymptotic examples, which are diagnostic only. It does not certify the unbounded-size statement; the proof in `RESULT.md` does.

The comparison with previous published OU-design results is necessarily limited where full primary text was not accessible. Independent audit: not performed.
