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

# Verification of the mathematical claim

The analytical proof evaluates the exact positive Green/Kac second-moment expression and its centered derivative, substitutes the upper incomplete Gamma function, applies its controlled large-argument expansion, and evaluates the subcritical integral with a positive Fubini--Beta calculation. A separate spatial strong-Markov/martingale argument establishes the centered subcritical limit. These steps, not sampled calculations, establish the infinite-distance statements.

## Reproducible checks

Run `python checker.py` with Python 3, `mpmath`, and `sympy` available. In the package tested here, the command returned `PASS: 198 independent symbolic/numerical assertions`. It checks the prescribed-mean generator equation, the centered second-moment ODE, an exact \(\alpha=3/2\) variance polynomial, the constant-force \(\alpha=1\) law, the \(\alpha=1/2\) Gamma constant, numerically split plateau integrals, and large-distance derivative ratios.

## Boundaries of verification

No numerical integral at finite distance is an exhaustive proof of a limit, and the checker does not simulate stochastic trajectories or independently validate publication priority. The proof does not address approximate mean profiles, finite observation noise, the excluded \(\alpha=2\) endpoint, or a central limit theorem above the variance boundary. Scientific independent audit has not been performed.
