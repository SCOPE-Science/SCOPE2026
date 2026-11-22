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

# Reproducibility and limits

Run `python verification.py` with Python 3, standard library only. The script constructs the graph from each binary word beginning in `0` and ending in `1`, computes true-twin classes from closed neighborhoods and tuft counts from vertex degrees, and separately computes both invariants from alternating runs. It verifies every possible canonical word at orders \(2\) through \(12\), confirms distinct degree multisets, and checks coefficientwise the rational cumulative generating function at all 49 bound pairs \(0\le p,q\le6\). It also checks the Fibonacci and power-of-two marginal identities.

Expected final output includes:

```
n=12 types=1024 sibling_zero=55 tuft_zero=512 PASS
CUMULATIVE_COMPARISONS 539
VERIFY_OK
```

These finite checks do not establish any claim for larger orders. The general proof is the run decomposition and exact enumeration in `RESULT.md`. The checked mathematical assumptions include the standard uniqueness of connected threshold creation words. No independent audit or external formal proof has been performed.
