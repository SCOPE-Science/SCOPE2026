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

The independent mathematical audit has not been performed.

## Direct finite checks

Run `python3 CHECK.py` in the directory containing this file and `CHECK.py` with an ordinary Python 3 interpreter. The script checks 210 Domb values using the original binomial sum, compares 384 finite-block correlations with the rational carry recurrence, checks 24 adjacent sign-pair cells and three exact low-shift formulas for six depths, and tests all stated nonzero-shift extrema and their equality classifications through shift 100,000. Actual execution printed `PASS` on all assertions.

## Proof-dependent infinite assertions

The multinomial-square representation and Lucas digit factorization establish the sign word at every index. The five carry coefficients and induction establish limiting rational correlations and their exact equality cases. The aligned-block estimate proves the arbitrary-cutoff error. Finite tests alone neither prove rational limits nor rule out larger extrema at untested shifts.

## Scope

All congruences concern the quadratic character modulo five, not square status in a local ring. Literature comparisons have unresolved historical-priority risk from general digit-multiplicative autocorrelation theorems.
