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

## Reproduction
Save the accompanying `verify.py` in the same directory and run `python verify.py` with Python 3, SymPy, NumPy, and SciPy. A successful check prints `VERIFY_OK` after displaying exact symbolic identities and period-averaging diagnostics.

## Checks actually performed
The script derives the Hopf normal-form coefficient from canonical-coordinate partial derivatives, checks the required equilibrium algebra and evaluates two exact rational predator-mean coefficients at a shared positive \(\alpha\). It then integrates the positive disease-free ecological system, extracts the last full upward-crossing period at \(\varepsilon=0.004\), and compares numerical mean shifts and prey variances against the local theorem. Both cases return the predicted opposite signs. The mathematical proof in `RESULT.md` is needed for the all-sufficiently-small-\(\varepsilon\) statement; numerical evidence alone does not prove that quantifier.

## Limits
The symbolic checks assume the valid Hopf normal-form formula, which is explicitly reconstructed in the proof. Numerical integration uses finite precision and finite time; the critical sign and sign reversal are certified by exact fraction algebra plus the analytic asymptotic expansion, not by integration. Independent audit was not performed.
