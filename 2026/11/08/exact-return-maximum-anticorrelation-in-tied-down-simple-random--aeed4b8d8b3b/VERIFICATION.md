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

# Reproduction and limits

From the directory containing the embedded files, execute `python verify.py` with Python 3.9 or later. Only Python's standard library is required. The checker independently tabulates exact moments for uniform simple symmetric bridges using (i) a finite-state dynamic program for half-lengths 1 through 40 and (ii) explicit combinations of increments for half-lengths 1 through 9. Each generated rational value is compared to the formulas in `RESULT.md`; the sign assertions are checked separately. The expected output is `PASS 432 exact rational identities; DP n=1..40, exhaustive n=1..9.` followed by the exact small-size covariance.

These finite checks are neither an exhaustive examination of all lengths nor a computational substitute for the proof. The infinite sign follows analytically from a strict ratio identity, and the limits follow analytically from Stirling's formula. No independently administered audit has been performed.
