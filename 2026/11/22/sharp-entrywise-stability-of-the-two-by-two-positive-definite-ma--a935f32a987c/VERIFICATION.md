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

# Reproduction and limits

The mathematical proof uses the matrix square-root Lyapunov derivative, its positive exponential kernel in the two-by-two Stieltjes orientation, and exact one-variable calculus. All data and constants are explicit in `RESULT.md`.

Run the included standard-library checker with `python3 check_square_root.py`. It independently evaluates the derivative via the three-variable Sylvester system and verifies its norm by all eight input-sign vertices. It checks the integral row representation, exact candidate bound at randomized spectral windows, finite differences, the near-endpoint `pi/8` witness, and the high-contrast limit. On the reviewed package, its output was `PASS: 16515 supplementary analytical-derivative, finite-difference, and window tests`.

Numerical checks are neither proofs for infinitely many matrices nor independent validation. The exact derivative factorization, order comparisons, and limiting extremizers are verified analytically in `RESULT.md`. Any literature-priority assessment remains provisional.
