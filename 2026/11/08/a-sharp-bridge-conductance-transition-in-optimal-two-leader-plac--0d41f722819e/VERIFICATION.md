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

The exact-rational verifier `verify.py` is self-contained and requires only Python 3. Replay with `python3 verify.py`.

Actual replay output:

```
VERIFY_OK: 114 exact rational graph-weight cases, 5109 exhaustive leader-pair objectives, 10 two-class threshold cases; exact sign-identity comparisons passed
```

Checks: builds the full weighted combinatorial Laplacian independently of the quotient formula; removes each unordered pair of vertices; computes the exact inverse trace via rational Gauss-Jordan elimination; compares it to the full eight-type table; checks optimal classes including exact-threshold ties; and separately tests all displayed sign identities at rational parameters.

**Limits.** Finite enumeration does not certify all positive real bridge weights or arbitrarily large graphs. The theorem's infinite-domain proof is the quotient-space calculation followed by rational sign factorizations in `RESULT.md`. A full independent audit has not been performed.
