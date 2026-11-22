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

The standalone `check.py` requires Python 3.10 or later and only its standard library. From the extracted directory run:

```bash
python check.py
```

It compares the exact all-width formula against independent coin-change dynamic programming for 3,429 parameter pairs, checks cumulative partial counts against a separate dynamic-programming implementation in 860 instances, tests the finite uniform rounding bound and the exact plateau in 77 cases, and exercises 54 examples of the cumulative profile bound. The three numerical mesoscopic samples are illustrations, not validation of an infinite asymptotic. Reproducibility does not amount to an independent scientific audit.

The written proof independently handles all integers \(a\ge2\), \(k\ge1\), all real cutoffs \(s\in[0,1]\), open gap endpoints, and the two distinct asymptotic scaling regimes. The main premises used are elementary properties of integer-interval semigroups and square-root sums; no external code or unpublished certificate is required.
