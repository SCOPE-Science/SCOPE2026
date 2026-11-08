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

# Verification of the Gaussian trajectory-error law

The proof in `RESULT.md` supplies an explicit deterministic remainder estimate and a Lindeberg–Cramér–Wold argument for all fixed real matrices and all fixed positive terminal times. Every finite-step risk computed below is independent of the stochastic signs because a second-moment operator recurrence evaluates their complete expectation. The numerical values are corroborating tests, not proofs of a limit.

Run `python check.py` with Python 3, NumPy, SciPy and SymPy. The checker passed symbolic commutator and local expansion tests, followed by seven finite-grid exact expectation comparisons. For the two-dimensional oscillator, scaled squared-error coefficients at step counts 4, 8, 16, 32, 64, 128 and 256 were approximately 0.5160771741, 0.5072623814, 0.5035147300, 0.5017415972, 0.5008687519, 0.5004341137 and 0.5002170205. The proved limit is exactly 1/2.

Unproved extensions: infinite-dimensional generators, nonlinear vector fields, dimension-uniform error constants, time intervals increasing with the step count, and distributional convergence rates. No independent audit was performed.
