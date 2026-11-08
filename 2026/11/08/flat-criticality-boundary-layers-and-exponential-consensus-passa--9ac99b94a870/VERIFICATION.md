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

# Verification notes

To reproduce: execute `python3 verify.py` using Python 3 with the standard library. Successful output for the included implementation is `VERIFY_OK 2352 exact and numerical checks`.

The script independently constructs finite-state transition matrices over rational arithmetic for \(2\le m\le11\) at \(\alpha=1\) and \(\alpha=2\), checks stationarity, reflection symmetry, the stationary product formula, and evaluates first-entry expectations by independently solving the linear system and comparing with the reversible telescoping formula. It checks the exact harmonic expression at \(\alpha=1\). Additional floating checks test mode inequalities across parameters and sizes, geometric boundary ratios, centered variances and the potential-barrier exponential rate at finite sizes. All numerical asymptotic comparisons use explicitly stated finite tolerances in the script.

These checks test derivations but do not prove asymptotic or universal claims on their own. Those depend on continuous endpoint extension of the ratio, uniform Riemann-sum approximation, geometric tail domination, local quadratic Laplace asymptotics, and the first-step telescoping argument in `RESULT.md`. No Lean or external formal certification was used. Independent external audit has not been performed.
