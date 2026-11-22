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
# Reproducibility

Run `python3 checker.py` with Python 3 standard library only. The checker explicitly enumerates idempotent maps, colourings and automorphisms for \((q,n_{\max})=(1,6),(2,5),(3,4)\), and compares both isomorphism and labelled order-two counts against a separate finite polynomial construction. It also verifies the sharp degree, lack of interior gaps and \(q^2\) top coefficient for \(1\leq q\leq5\).

The recorded terminal output is:

```
FORMAL_CHECKS [(1, 6, 8, 1, 1), (2, 20, 3072, 2, 6), (3, 65, 805306368, 3, 15), (4, 198, 2951479051793528258560, 4, 28), (5, 567, 701520785918833400737768719703815849434847620628480, 5, 45)]
DIRECT_CHECKS [(6, 1308), (5, 7022), (4, 3621)]
ALL_CHECKS_OK
```

Finite tests verify only the enumerated cases. The all-size proof is the independent group-factorization and subset-sum argument in `RESULT.md`. The checker does not verify literature priority or independent audit status.
