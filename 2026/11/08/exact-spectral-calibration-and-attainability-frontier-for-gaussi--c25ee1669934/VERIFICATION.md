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

Run `python3 verify.py` with Python 3.10 or newer; no third-party packages are required. The deterministic script checks Gaussian posterior KL against the reduced scalar objective (up to its constant), stationarity and positive-minimiser formula, sign comparison with EEA, boundary cases, and independent complex-step derivative tests. It prints `VERIFY_OK` only if all assertions pass.

In addition, a separately executed NumPy stress experiment compared the proposed three-dimensional diagonal optimizer against 5,000 arbitrary SPD noise precision matrices over 500 sampled spectra. It found no counterexample; this sampling is not exhaustive and does not itself prove global optimality. The analytic proof in `RESULT.md` gives the all-dimensional and boundary conclusion through strict convexity, symmetry reduction and the scalar derivative sign.

The scientific result has had a self-review. Independent external proof checking, historical-priority certification and independent numerical validation have not been performed.
