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

# Verification and reproducibility

Run `python3 verify.py` using Python 3 and its standard library only. The checker independently builds the full absorbing transition matrix for a random walk with one-step resets, solves rational hitting-time equations by elimination, and evaluates the Chebyshev formula by recurrence. It covers every integer \(1\le k\le n\le18\) and reset rates \(0,1/11,1/4,3/5\). In addition, it tests the exact polynomial coefficients (including the second coefficient that defines the transition) and checks all of their signs in the non-beneficial region through those sizes.

The completed checker output is `VERIFY_OK 1881 exact assertions`. The checks require no external data and assert exact equality of fractions, not floating-point agreement. The analytic proof applies to all positive lengths, not just the test range. Full mathematical independence, priority, uniqueness of the positive optimum, alternate boundary types, and finite-sample inference are not established by this package.
