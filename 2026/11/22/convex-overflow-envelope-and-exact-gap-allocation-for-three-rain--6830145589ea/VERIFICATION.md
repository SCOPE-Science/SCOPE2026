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

# Verification record

The analytical proof is in `RESULT.md`. The local reproducibility check is the standalone Python standard-library file `verify.py`.

Run `python3 verify.py` in the directory containing `RESULT.md` and the script. The verified execution reported:

```
PASS 88156 exact or controlled-tolerance assertions
```

The independent recurrence implementation uses rational arithmetic for pulse additions, retention multipliers, storage clipping and spill. Tests compare it to the explicit convex envelope; sample midpoint inequalities and the no-extra-spill interval; compare a finite list of theoretical candidate minima to a dense numerical grid; and verify the rational parameter examples and selected cases of the unbounded equal-gap ratio family. Floating-point calculations are restricted to candidate square roots and objective-grid comparisons, with a \(10^{-11}\) numerical tolerance there. The checker uses no data files or external dependencies.

Critical proof steps that must not be inferred from code are: the exact saturation-case identity for the four-branch maximum; convexity and full enumeration of possible switching points; proof of uniqueness of every strictly positive additional-spill minimizer; precise algebraic conditions for the smooth two-overflow regime; and the exact all-integer family producing arbitrarily large ratios. These are argued symbolically in `RESULT.md`. No exhaustive historical-priority or independent external validation has been performed.
