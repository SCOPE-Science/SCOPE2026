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

# Reproducible finite checks

Run `python3 verify.py` with Python 3 and no additional packages. The program generates the period-doubling word by repeated substitution and explicitly computes distinct factors, rotations, and their intersections. It checks all odd lengths from \(1\) through \(129\) and verifies the explicit three-member class construction for \(j\in\{1,2,3,4,5\}\), corresponding to lengths \(5,17,65,257,1025\). It also compares factor sets between consecutive large substitution prefixes as a finite-sample stability check.

Expected and observed output:

```
VERIFY_OK odd_lengths=65 sharp_constructions=5
```

Finite enumeration cannot prove universal validity or all-length factor-language completeness. The proof of the universal ceiling and infinite witness family is purely symbolic and is in `RESULT.md`. Independent audit has not been performed.
