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
# Reproduction and limitations

Run `python3 checker.py` using Python 3.9 or later with no third-party dependencies. It prints `PASS transfer/GF=112; independent distinct-word enumeration=73; finite balance=190` after comparing the exact two-state polynomial transfer, the rational generating-function recurrence, direct enumeration of distinct output words for source lengths at most 19, and the fixed-period balancing assertion over specified bounded instances. The checker verifies coefficients of the complete length profile; it does not validate arbitrary parameters beyond those in the code.

The mathematical proof is in `RESULT.md`. In particular, the formal identity for all positive \(a,b\) follows from an exact one-letter update and symbolic resolvent; positivity of derivative coefficients proves the all-period constrained extremum; pole analysis proves the growth base. Independent audit has not been performed; historical novelty is conditional on the literature comparisons described in `REVIEW.md`.
