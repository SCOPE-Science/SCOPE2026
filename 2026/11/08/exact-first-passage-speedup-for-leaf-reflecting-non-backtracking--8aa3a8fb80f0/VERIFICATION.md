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

The self-contained `verify.py` is executable with Python 3 and no third-party packages. Run `python3 verify.py` in the same directory. Its final line was:

```
VERIFY_OK exact independent comparisons = 4202
```

The checker derives two independently constructed absorbing first-step systems (ordinary vertex chain and persistent directed-edge chain), solves them over exact rational numbers, and compares every result with the theorem formula. It checks every source-target pair of all recursively labelled trees on two through six vertices, plus representative trees up to ten vertices. The code and data are embedded with the mathematical documents. This finite set of checks supports reproducibility but does not replace the general induction, and no external independent validation is asserted.
