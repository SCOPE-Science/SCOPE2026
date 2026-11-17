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

# Reproducible mathematical verification

Run `python verification.py` in an environment with `numpy` and `sympy`. The script rebuilds the reflected Hessian and the first-order state matrix from the stated quadratic energy; checks the exact characteristic polynomial and its factorization at the critical root; compares 1,000 deterministic positive parameter quadruples with the predicted stability classification at six distinct angles each; and checks a worked unit-curvature counterexample.

The script prints `PASS`, the critical angle in radians and degrees, and the full four-by-four eigenvalue spectrum for the \(30^\circ\) example. The script is numerical/symbolic cross-checking; the infinitely quantified classification follows from the exact block determinant, strict Routh--Hurwitz inequalities, and analytic critical factorization in `RESULT.md`. The tested angular grid is not claimed to exhaust real angles or parameters.

All critical identities can also be reproduced by hand:

\[
\det K=uv,\qquad\operatorname{tr}K=(u+v)\cos2\theta,\qquad
P(\lambda)=\det((\lambda^2+\gamma\lambda)I_2+\omega K).
\]

No independent external audit or certification was performed. The cutoff at \(\theta_*\) concerns a fixed projector; it is not a bound for dynamically changing projector approximations.
