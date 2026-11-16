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

The analytical theorem is established by exact Boolean shell moment identities, an explicit two-atom variance equation, a two-dimensional convex-hull theorem, and modular arithmetic. The standalone `check_two_shell.py` uses only Python's standard library and rational arithmetic.

Actual replay on the packaged scientific files produced:

```text
QUADRATIC_WALSH_TWO_SHELL_PASS moments=4..10 exact_gram=6,8 modular_orders=4..3000 infinite_families=checked
```

In particular the exact Gram check is independent of the closed-form shell moment identities and uses individual Boolean vertices. The modular computer checks are finite corroboration, not an exhaustive proof beyond dimension 3000. The full all-dimension conclusions rely on the proof in RESULT.md.
