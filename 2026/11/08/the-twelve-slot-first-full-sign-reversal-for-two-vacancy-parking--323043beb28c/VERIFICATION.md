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

# Verification of the finite covariance classification

Execute `python CHECKER.py`. The deterministic construction computes \(W_{a,b}\) as an integer via factorials and Cayley parking counts, then computes \(Z\), \(H_i\), and integer numerators \(Q_{i,j}\) exactly. All signs are strict; \(n=12\) has 11 positive adjacent and 55 negative nonadjacent pairs.

The program also cross-checks the two-vacancy weights against direct enumeration of all-right preference words for \(n\le7\), and independently against subprobability dynamic programming for several constant and time-varying biases. Its 410 assertions passed on the packaged source in the current execution. These finite tests do not prove unbounded statements, but the only claim beyond the finite certificate—direction-bias invariance of the set weights—is established analytically by the block-counting and convex-kernel arguments in RESULT.md.

The published block counts and their generalizations are acknowledged as established results. The 12-site sign matrix and minimality are the assessed new claim. No other values of \(n\) greater than 12 have been certified by this package. Historical priority is not independently certified.
