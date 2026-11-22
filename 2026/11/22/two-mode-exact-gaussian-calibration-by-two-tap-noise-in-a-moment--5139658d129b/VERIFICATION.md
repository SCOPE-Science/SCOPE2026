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

The supporting `verify.py` uses only Python standard-library `fractions.Fraction` and `random.Random`. It builds the three-state augmented covariance equation independently of the closed form and solves its 9-by-9 rational system to check the stationary variance formula. It then checks the real-tap feasibility inequalities, the two-point interpolation identity, the exact signed error factorization, a rational two-mode example, and the zero-momentum boundary. It prints a pass count on successful completion.

Run from this directory with `python verify.py`. Numerical experiments are not used as a proof of global stability or of the arbitrary-dimensional result. The proof in `RESULT.md` establishes those by algebra and the Schur/Jury stability conditions; the finite tests only guard against implementation and arithmetic errors. No independent mathematical audit was performed.
