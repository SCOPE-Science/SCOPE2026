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

# Verification and limits

The exact theorem is established by the initial-set classification, cyclic-interval counting bijection, coefficient-difference proof and log-concavity boundary argument in RESULT.md. None of the infinite-parameter statements relies on a finite search.

`VERIFY.py` requires Python 3.9 or later and uses no third-party dependencies. Execute `python VERIFY.py`. It constructs graphs directly from their cycle and pendant-path edge lists, enumerates all initial subsets of 34 instances, independently checks induced connectedness and sequential zero forcing, then compares the all-size distributions. It also performs 1,680 separate coefficient-shape checks.

Observed output:

```
DIRECT_ALL_SUBSETS_OK instances 34 subsets 46608
COEFFICIENT_AND_SHAPE_FORMULAS_OK cases 1680
VERIFY_OK
```

The exhaustive checks cover only \(3\le c\le9\), \(1\le t\le5\), \(c+t\le13\); the arithmetic checks cover \(3\le c\le50\), \(1\le t\le35\). They are empirical cross-checks, not infinite proofs. Independent mathematical audit has not been performed. Literature searches do not establish absolute historical priority.
