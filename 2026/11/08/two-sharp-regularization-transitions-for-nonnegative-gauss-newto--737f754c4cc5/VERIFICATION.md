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

# Reproducibility and scientific limits

Run `python artifacts/verify.py` using a standard Python 3 installation; no packages, network, or external files are required. `artifacts/verification.txt` records the actual program output obtained before packaging.

The executable checks 37,727 assertions, including rational examples, exact objective-to-variance identities, sharp endpoint mixtures, finite-scale optimum, and randomly generated diagonal SPD spectra. The infinite/all-dimensional claims, global maxima and uniqueness are analytically proved in `RESULT.md`; a finite test suite cannot independently certify those quantifiers.

The scientific analysis is reviewed within this package. Independent validation has not been performed.
