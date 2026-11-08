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

# Computational verification and its limits

Run the supplied `check.py` using Python 3 standard library: `python check.py`.

The tests enumerate each set partition at sizes \(n=1,\ldots,8\), including all 4,140 partitions of size eight. They verify Bell counts; the exact prescribed-singleton probability and joint disjoint-window factorial moments; the conditional mean endpoint gap formula; strict Bell-number log-convexity for \(2\le n\le600\); and exact inclusion–exclusion/no-singleton-window counts with finite-scale diagnostics. The checker reports 1,106 successful checks.

An exact finite enumeration does not establish convergence as \(n\to\infty\). The process limit uses the Bell-number asymptotic and factorial-moment convergence; the expected-gap limit uses a fourth-moment tail argument. Results beyond the stated scopes, quantitative rates, and historical originality are not verified by this code.

Independent audit is not performed.
