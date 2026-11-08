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

# Finite checks and analytical proof boundary

The supporting self-contained script `artifacts/verify.py` uses Python 3 standard-library `fractions.Fraction` and `itertools.product`; it requires no downloaded data. It enumerates every sequence of parent choices up to five births for one and two edges at each birth, at geometric parameters \(q=1/2\) and \(q=1/3\). It verifies exact normalization and bounds for parent probabilities, exhaustive joint-law normalization, exact incoming-degree means and generating functions, total-edge consistency, and lower probabilities for full-hit blocks. Expected terminal output:

```
VERIFIED 61632 exact finite rational assertions
```

The main theorem is infinite and almost sure; no finite enumeration can verify its conclusion. Its proof instead uses the exponential-moment bound, a disjoint-block lower bound, summability on dyadic indices, Borel–Cantelli, and monotonicity. The assumed independence is precisely across all parent choices, including edges created at the same birth. No independent mathematical audit has been performed.
