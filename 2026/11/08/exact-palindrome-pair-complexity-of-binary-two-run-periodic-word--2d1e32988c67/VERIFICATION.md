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

# Verification

A direct proof appears in `RESULT.md`. The code `verify.py` independently constructs all cyclic-phase factors for run lengths 1 through 9 and lengths up to four full periods. Dynamic programming over all palindromic substrings determines the minimum factorization length; the program checks both the coefficient identity and the necessary/sufficient interior-phase condition. All 3,240 parameter-length configurations, 36,720 phase tests, and 36,720 word checks passed when executed with Python 3.

Run with `python3 verify.py` in the directory containing this file. No third-party Python packages are needed. These checks are bounded examples, not an exhaustive proof for arbitrary parameters. The unbounded proof requires the run-endpoint cut argument and phase injectivity presented in `RESULT.md`.

The scientific literature assessment is comparative and not a claim of independent validation, formal certification, or bibliographic exhaustiveness.
