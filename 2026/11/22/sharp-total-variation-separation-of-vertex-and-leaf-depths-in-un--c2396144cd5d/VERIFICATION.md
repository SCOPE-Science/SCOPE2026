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

# Reproducible checks and limits

Run `python3 checker.py` from the package directory. Python standard library only. The test independently enumerates all \((n-1)!\) uniform recursive trees for \(2\le n\le8\), including ordinary leaf-first and leaf-size-biased depth histograms, exactly compares generating distributions and variances via rational arithmetic, and confirms the finite-size TV bound. It then computes numerical Poisson-binomial modes at three much larger sizes, solely as asymptotic sanity checks. Expected output terminates `PASS 99 assertions`.

These finite tests do not certify the universal theorem: the proof uses the generating-function recurrences, a variance identity, an exact unimodality fact, and a local central limit theorem derived from characteristic-function bounds. No external independent assessment was performed.
