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

# Reproducibility checks

Run `python3 verify.py` using Python 3 and only the standard library, with no external datasets. The verification code directly checks the three-by-three coefficient matrix identities and Gaussian-Ritz discriminant with exact fractions; 14,400 exact rational checks are made. It also evaluates 20 independent angular-integral parameter cases and performs 180,000 seeded two-by-three Gaussian sketches for the exact sharp SPD example.

Observed replay: `VERIFY_OK exact_rational_identities=14400 angular_checks=20 gaussian_trials=180000 empirical=0.1844722 predicted=0.1835034 tolerance=0.0063865`.

Finite random trials are neither exhaustive nor infinite-dimensional verification. The universal inequality, sharp equality family, exact probability integral and vanishing degeneracies depend on the algebraic Gaussian proof in RESULT.md. No independent mathematical audit has been performed.
