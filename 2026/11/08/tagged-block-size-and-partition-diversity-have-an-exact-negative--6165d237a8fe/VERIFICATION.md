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
# Verification summary

Run `python3 verify.py` with Python 3 and its standard library. The checker constructs the probability law of \((S_n,K_n)\) from the elementary seating transitions and checks two means, two variances and one mixed covariance against independently derived rational formulas, as well as negativity. It has passed **1392 exact moment-and-sign checks** at eight rational parameter pairs, including \(\alpha=0\), \(\theta=0\) with positive discount, and allowed negative \(\theta\), for all \(2\le n\le30\).

The analytic proof in RESULT.md separately establishes the all-size, all-admissible-parameter claims by a closed covariance recursion, a beta-binomial variance identity, a second moment recursion, and Gamma-ratio asymptotics. Enumeration is finite support only and cannot prove infinite claims or priority. No independent audit has been performed.
