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

# Reproduction

Run `python3 verification/check.py` from the package root using Python 3 standard libraries. Expected captured output appears in `verification/output.txt`: `PASS: 33062 assertions; exact rational, direct matrix and angular-integral checks`.

Tests use exact fractions for all integer spectral ratios from 2 through 30, candidate counts from 1 through 11, and rational orientation parameters from 0 to 1 in increments of 1/100. They also compute Nyström residuals directly from the defining matrix formula at four angles across five positive spectra, and independently check numerical circle integration for Gaussian probes. Finite tests do not establish convexity, full parameter quantifiers, or the Gaussian integral: those are proven in the manuscript. Checks performed with complete package paths and output reproduced. No independent scientific audit was performed.
