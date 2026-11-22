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

# Verification evidence and limits

The mathematical verification is a discounted-cycle renewal calculation coupled to one-dimensional diffusion boundary-value equations, short-time killed OU semigroup estimates, a one-sided derivative jump at the home position, and dominated convergence under \(\mathbb EW^2<\infty\). The proof establishes the pointwise Laplace-transform asymptotic for every fixed \(s>0\) and every admitted independent clock; it does not rely on numerical extrapolation.

For a finite-rate check, run `python CHECKER.py` with SciPy and NumPy. The script uses the exact killed Brownian Green kernel for exponential alarm intervals and the killed Brownian heat kernel for deterministic alarms, plus a parabolic-cylinder-function solution of the return OU equations. It evaluates the completion transform by **two independent finite-rate expressions** (discounted-potential difference and direct renewal success numerator), checks the return ODE and boundaries, and compares scaled transform differences at multiple rates and Laplace parameters. The packaged implementation passed 217 numerical and analytic-consistency assertions. A separate direct high-rate calculation gave, at return stiffness \(2\), search stiffness \(0\), and \(s=0.75\), limiting coefficients approximately \(1.6342130248766844\) (Poisson) and \(0.7241417922856578\) (periodic), with ratio \(4/\sqrt\pi\approx2.256758334191025\). Finite tests do not prove uniformity, error bounds beyond the stated \(o(r^{-3/2})\), or generalization beyond the listed assumptions.

The prior published \(r^{-3/2}\) **mean** result is credited; the checked new statement is the nonconstant \(s>0\) transform coefficient. No independent validation has been performed.
