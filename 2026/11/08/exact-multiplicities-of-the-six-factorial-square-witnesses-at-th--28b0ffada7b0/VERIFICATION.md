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

# Reproducibility

Run `python3 artifacts/verify.py` from the directory containing `artifacts/witnesses.csv`. The program uses only the Python 3 standard library. It checks the complete witness CSV against two independent exact enumerations, one using trial-factored integer parity and the other Legendre's factorial valuation formula. It prints `VERIFY_OK n=527 count=132` and the penultimate-index profile on success.

The exhaustive search is finite because the prime \(523\) forces the penultimate index to one of \(523,524,525,526\). Both enumerations loop over all possible prior ordered index pairs and enforce the strict inequalities, without random sampling. The complete witness CSV is not merely a sample.

Known limits: this only settles the exact witness multiplicity at maximum index \(527\). Prior literature establishes that this is the first six-factor boundary; this package does not independently prove the entire historical least-boundary theorem. Independent mathematical audit and historical-priority verification have not been performed.
