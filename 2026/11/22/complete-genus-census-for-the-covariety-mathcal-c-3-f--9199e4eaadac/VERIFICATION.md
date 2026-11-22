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

# Verification performed

The included `verify.py` uses the standard Python library only. The first check builds all subsets of positive integers below each Frobenius number in the inclusive range 4–18, retains precisely the closed cofinite additive submonoids with 3 pseudo-Frobenius, then compares their genus histogram against the three-tail normal form. The second check independently enumerates the tail-parameter regions and compares every genus coefficient and the total cardinality for all Frobenius numbers 19–750. Exact integer arithmetic is used throughout.

Running `python3 verify.py` produced:

```
VERIFY_OK 747 parameter values; exhaustive F=4..18; formulas F=4..750
```

This is not a formal proof for unbounded parameters; the proof in `RESULT.md` gives the quantifier-complete argument. No external validation has been conducted.
