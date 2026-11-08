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
# Verification and limits

The closed-form stationary covariance follows from a three-dimensional linear-state system and is independently derived by causal convolution. Reproduce the computational checks with `python CHECK.py` from this same package (requires SymPy, NumPy and SciPy). The script verifies stationary covariance symbolic identities, the critical amplitude gap, exact spectral-ratio algebra, and independently computed matrix-exponential correlations. It additionally samples finitely many parameter/time points only as a diagnostic. Finite sampling cannot demonstrate positivity or exclude late sign changes; the analytic proof provides those conclusions.

The oscillatory asymptotic argument assumes \(\Omega>\alpha\) fixed before \(\lambda\downarrow\alpha\); the boundary is strictly positive for every finite lag. The result does not cover independent thermal white noise, nonstationary initial states, or forcing with nonexponential two-point covariance. No independent audit or external scientific certification has been performed.
