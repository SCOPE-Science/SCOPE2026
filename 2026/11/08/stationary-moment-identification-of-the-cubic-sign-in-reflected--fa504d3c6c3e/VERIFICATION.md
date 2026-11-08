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

The analytical argument derives the stationary density from the no-flux condition, proves the fixed-variance monotonicity through strict covariance inequalities, and obtains the rational formulas from two integration-by-parts equations with boundary-vanishing test functions.

To repeat finite diagnostics, install the specified dependency from `requirements.txt` and execute `python verify.py` in the extracted directory. It checks eight parameter tuples at 65 decimal digits, compares the reconstructed drift/noise ratios to input values, and verifies the two-moment sign test, including the zero-cubic boundary. It also constructs opposite cubic signs with the same second moment. Expected output: `PASS 26 numerical checks; 8 parameter cases and same-variance sign separation`.

These numerical checks do not prove an infinite family of identities. The mathematical proof is in `RESULT.md`. The sign conclusion is for exact stationary moments; finite-sample estimation, quasistationary conditioning, and unknown reflecting endpoints have not been validated. Independent audit has not been performed.
