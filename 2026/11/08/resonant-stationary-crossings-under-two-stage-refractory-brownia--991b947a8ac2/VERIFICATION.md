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

# Verification and reproducibility

Run `python checker.py` from the extracted artifact directory with Python, SymPy, NumPy, and SciPy installed. The checker validates the three-state Markov resolvent and stationary pole in exact symbolic arithmetic, checks special-point coefficients, and numerically cross-validates explicit moments against independently integrated forward moment equations. It also checks finite root counts close to the isolated cancellation point on both parameter sides.

These checks do not independently establish uniqueness in the literature, certify exact infinite zero counts by experiment, or substitute for the analytic lobe-count argument in RESULT.md. The published record and its alternatives were examined for statement-level overlap; independent scientific audit remains unperformed.
