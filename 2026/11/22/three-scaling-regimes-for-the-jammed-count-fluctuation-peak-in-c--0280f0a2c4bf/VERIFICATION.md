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

# Reproducibility and limits

Run `python verify.py` with Python 3, SciPy and NumPy installed. The script evaluates regularized incomplete beta functions for the four charge-kernel cases, compares the derived mixture against explicit sixteen-channel enumeration, verifies the strict monotonic crossing numerically, solves the unique variance-peak condition, and checks the three claimed asymptotic regimes at several small positive interaction offsets. A separate random beta-sampling experiment corroborates the exact binary probability within stated sampling tolerance.

The analytic beta-integral estimates, monotonic bracketing and critical-window balance are the proof. Finite parameter checks and finite simulations cannot establish convergence for all small interaction offsets or prove novelty. The related 2025 journal full text was not independently inspected; the inspected 2026 primary source and its formulas, together with available metadata and indexed prior claims, define the evidence and priority limits.
