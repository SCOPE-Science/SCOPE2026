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

# Computational verification and scope

Run `python3 verify.py` in the directory containing the extracted files. The script requires only Python's standard library. It enumerates all three-state assignments and verifies the four disjoint probability classes against independent rational counting for \(1\le a,b\le4\) and activities \(1/4,1/2,1,2\). It separately runs finite-size log-weight calculations against the limiting probabilities at representative values and checks the limiting monotonicity and reentrance behavior on grids.

The exact verification compares 64 finite partition identities, the asymptotic suite evaluates 60 parameter/size combinations, and seven imbalance parameters are used in the monotonicity suite. All passed in the packaged version. None proves the infinite-size theorem; that follows analytically by partitioning states, explicit logarithmic expansions, conditional binomial concentration, and the strict decrease of \(\tanh(t)/t\).

The asymptotic tests use a numerical tolerance and cannot establish existence, uniqueness, or absence of extrema outside the sampled grid. The analytic argument covers all \(\kappa\ge0\) and fixed \(c>0\). No independent scientific audit has been performed.
