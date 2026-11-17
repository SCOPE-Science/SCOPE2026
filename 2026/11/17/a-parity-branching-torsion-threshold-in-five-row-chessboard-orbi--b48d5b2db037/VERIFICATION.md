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

Exact reproducibility check: `python3 a5_quotient_verify.py` under Python 3.13 and SymPy 1.14.0.

Recorded output:

```
A5 orbit enumeration: PASS
n=4: H3 free=1, torsion=[]; H4 free=0; D^2=0 PASS
n=5: H3 free=4, torsion=[]; H4 free=0; D^2=0 PASS
n=6: H3 free=9, torsion=[]; H4 free=1; D^2=0 PASS
n=7: H3 free=14, torsion=[3]; H4 free=6; D^2=0 PASS
n=8: H3 free=14, torsion=[3, 3, 3, 3, 3, 3, 6]; H4 free=21; D^2=0 PASS
ALL EXACT CHECKS PASSED
```

The implementation enumerates all sixty even permutations on five labels and verifies the one-orbit/two-orbit classification, constructs quotient cellular differentials with signed face deletion, checks every adjacent boundary composition, constructs the smaller integral \([U\ R]\) presentation, and verifies its Smith diagonal against modular ranks of the original cellular maps. The handwritten proof of the presentation and of the passage from homology to homotopy is in `RESULT.md`. These checks cover exactly four through eight columns; smaller widths follow directly from the simplex model. No computation beyond eight columns or external independent validation is claimed.
