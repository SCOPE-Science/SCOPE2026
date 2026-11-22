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

# Reproducible checks

Run `python3 verify_bruteforce.py` and `python3 verify_series.py` using Python 3 and its standard library in the same directory as these files. The first program enumerates all binary positions of lengths zero to twelve and obtains Grundy numbers through literal legal-move mex recursion (8191 words). It checks the derived factorization, losing-class criterion and sharp extrema. The second program independently uses the Catalan first-return convolution through length seventy (1296 nontrivial bivariate coefficient positions), checks summation to all binary words and the explicit losing/magnitude formulas. Recorded outputs are in `verify_bruteforce.out` and `verify_series.out`. Infinite-domain correctness depends on the written factorization and recurrence proof, not on finite replay. Historical originality remains subject to possible unindexed work.
