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
# Reproducibility and scope

The `verify.py` program uses Python 3, NumPy and SymPy. Run `python verify.py` from the directory containing the files. It checks exact symbolic identities for the two-time fourth cumulant, unique critical lag and peak limits, and then evaluates the exact two-component Gaussian mixture in three deterministic-seed numerical scenarios. A two-dimensional Gauss–Hermite quadrature computes representative positive KL gaps against the matched Gaussian comparator. It prints the analytic and sampled fourth cumulants and KL values.

The printed sample comparisons and quadratures are finite illustrative checks, not proofs of continuous-parameter positivity, novelty or independence. The analytic arguments in `RESULT.md` cover every \(\lambda,D,r,t>0\). Reproducibility presumes a compatible NumPy and SymPy environment and ordinary floating-point reliability; the inequalities are established algebraically without relying on the Monte Carlo or quadrature signs.

No independent external scientific audit was performed. The one-time Gaussianity and detailed balance are exact features of the equilibrium-refresh design; they do not imply pathwise Gaussianity. The unique optimized lag concerns the connected fourth moment, not measured signal-to-noise or the mutual-information gap.
