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

The analytic calculation reduces stationarity to a finite resolvent and proves the unique optimizer and singular limit independently of numerical experiments.

Run `python verify_chiral_trimer.py` with Python, SymPy, and NumPy installed. The checker constructs the Hermitian triangle matrix, verifies the complete \(9\times9\) exact resolvent identities and determinant, and independently solves complex linear stationary equations for a parameter grid. It also verifies the optimizer derivative polynomial, its special factorization at maximum flux, the positive comparison identity for flux monotonicity, and the weak-flux limits.

Observed result: PASS, with 304 independent scalar numerical assertions in addition to exact symbolic checks. These tests do not constitute exhaustive numerical verification over a continuum; the proof in RESULT.md supplies the full quantifiers. No independent scientific audit or external certification has been performed.
