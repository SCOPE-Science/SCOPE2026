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

# Verification of trimer spatial correlations

Run `python3 verify.py` using Python 3 with no nonstandard modules. The reproducible checker evaluates every local probability by exhaustive integer subset recursion on the \(d+7\) relevant first-arrival clocks, with \(1\le d\le7\). The largest instance has fourteen clocks and at most \(2^{14}\) position subsets; no Monte Carlo approximation is used for any rational coefficient. It checks both marginal distributions against the known single-site law and independently simulates every possible arrival order for distances one and two directly under the sequential deposition rule.

The exact six lag covariances sum to the stated positive long-run variance. The proof in RESULT.md separately establishes finite dependence and the Gaussian limit for arbitrarily large \(n\); the finite arithmetic checker does not claim to certify an infinite theorem by enumerating finitely many cases. Independent audit has not been performed.
