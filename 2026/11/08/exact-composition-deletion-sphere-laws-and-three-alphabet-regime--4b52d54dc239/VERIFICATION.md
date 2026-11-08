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

# Verification and limits

Run `python3 checker.py` using Python 3 standard library. This computes direct deletion-sphere sizes from all prefix/suffix count vectors and compares the full exact distribution against the separate first-return convolution, for binary lengths through 14, ternary lengths through 9 and four-symbol lengths through 7. It compares rational mean formulas and checks renewal normalization through 13 for alphabet sizes 2–7. The completed run printed:

```
PASS exhaustive 84133 input words, q=2 through n=14; q=3 through n=9; q=4 through n=7
PASS independent renewal normalization for q=2..7, m=0..13; exact means and distributions
```

The proof in `RESULT.md` is necessary for arbitrary input length and the asymptotic limits; finite tests cannot establish either. The algebraic return series uses exact rational coefficients. The limiting arguments require an aperiodic, full-lattice random walk and fixed alphabet size. The reviewed evidence is not independent mathematical validation.
