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

# Reproducibility and verification
Run `python3 verify_cut.py` with standard Python 3. It independently decodes all Prüfer codes for 2–7 labelled vertices and compares the empirical cut histogram with exact integer coefficients of the weighted polynomial. It also checks rational exact expectation and variance, without simulation or floating-point tolerances. A completed run reported 21 distributions, 107877 Prüfer trees and successful moment tests. This finite calculation is not a proof of an asymptotic assertion: those rely on the eigenvalue formula, the stated Poisson couplings and the Poisson central limit theorem in RESULT.md. The remaining possibility of an unindexed prior equivalent is a priority risk; no independent external audit has been performed.
