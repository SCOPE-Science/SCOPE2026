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

# Reproducibility and verification

Run `python verify.py` with Python 3.9+ and SymPy 1.10+ in the same directory as the research documents. The script is self-contained except for the stated publicly available SymPy package; it needs no network access, data files, or random sampling.

The script independently solves six exact symmetric matrix Lyapunov equations by symbolic elimination and compares the result with the stated rational stationary variance. It checks the wrong-sign and lower-bound rational factorizations, the derivative at zero momentum, the \(q\to-1\) square-root expansion, and three exact rational numerical examples; the explicit covariance is substituted back into its Lyapunov equation for each example. These symbolic identities test the algebra; the inequalities, existence and optimizer compactness are proved in RESULT.md rather than inferred from experiments.

No physical experiment, machine-checked formal proof, third-party certification, or independent audit has been performed. The construction assumes finite innovation variance, a stable scalar recursion, and the stationary limit.
