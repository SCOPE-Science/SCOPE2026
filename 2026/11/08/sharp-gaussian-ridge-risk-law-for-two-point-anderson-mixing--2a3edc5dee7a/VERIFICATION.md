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

# Reproducible verification

Execute `python verify.py` with Python 3, NumPy, SciPy and SymPy. The supplied `verification_output.txt` records an actual execution with all 155 assertions passing.

Checks include a symbolic closed-form ridge minimizer and exact error identity; Gaussian Taylor coefficient \(A\) and \(Q(c)\) equality; 120 direct independently generated pairs of noisy evaluations compared to the formula; numerical Gauss-integral risk comparisons; normal-ratio tail coefficient; and numerical scale checks for the weak-ridge asymptotic. The two-noise variables used in the code match the model in `RESULT.md`.

These are finite independent checks. The analytic proof is needed for infinite moment divergence, convergence of the tail limit, the exact all-parameter square-root constant, and strict convexity in the fixed-coefficient small-noise expansion. The expansion is not a global finite-noise optimization statement. No independent audit has been performed.
