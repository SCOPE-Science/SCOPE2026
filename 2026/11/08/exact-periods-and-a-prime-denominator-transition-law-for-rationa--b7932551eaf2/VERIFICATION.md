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

Run `python3 verify.py` beside this file with Python 3 and no external packages. The script computes integer-part gcds without floating point, uses exact rational densities, and independently checks the least-period assertion by testing every prime-factor period reduction.

Actual execution returned:

```
EXACT_FLOOR_VS_RESIDUE_PERIOD_AND_DENSITY_OK cases= 33
EXAMPLE_P5_K2_OK
COSET_INVARIANCE_AND_EXACT_AVERAGE_OK cases= 120
VERIFY_OK finite_only=True independent_audit=False
```

These computations cover only stated finite parameters: the full periods of 33 triples with \(p\in\{2,3,5,7,11,13\}\), \(k\in\{2,3,4\}\), and \(a\in\{1,2\}\) with \(p\nmid a\); and 120 coset/mean combinations across 24 larger primes and five exponents. Their success is corroboration, not a proof for all parameters. The unrestricted statement relies on CRT and elementary modular arithmetic, and the uniform prime-denominator limit relies on the classical Pólya–Vinogradov inequality as explained in `RESULT.md`. No outside assessment has been performed.
