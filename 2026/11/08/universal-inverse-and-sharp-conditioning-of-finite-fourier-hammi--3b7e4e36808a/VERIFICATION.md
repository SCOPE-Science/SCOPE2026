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

Run `python hamming_ball_fourier_check.py` with Python 3, numpy and sympy. It constructs the Fourier matrices from cyclic and Klein-group bicharacters, evaluates the closed-form inverse independently, and checks both matrix products exactly for three cases. The same script tests six further cyclic/noncyclic configurations numerically, including the non-prime-power group order six, and verifies the derived Frobenius formula.

The expected completion marker is `FOURIER_HAMMING_BALL_INVERSE_CHECKS_PASS`. The calculations are finite cross-checks only; the infinite-dimensional asymptotic follows from the exact formulas and the degree-counting proof in RESULT.md. No independent mathematical audit has been performed.
