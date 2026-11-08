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

The standalone exact checker `verify.py` uses symbolic inversion of the seven-state transient Markov generator to verify both rational expectation formulas and their decisive differences and derivatives. It independently solves 240 rational generator systems using `fractions.Fraction` Gaussian elimination and checks 21 exact threshold/endpoint comparisons, all passed. The infinite-domain conclusion follows from positivity and factorization in `RESULT.md`, not from the finite grid. SymPy is required for the symbolic part of the reproducibility check.

The process has finite expectation for every finite nonnegative choice of two rates. The theorem permits one rate to be zero. No numerical simulation, empirical population data, stochastic-experiment extrapolation, or independent audit is claimed.
