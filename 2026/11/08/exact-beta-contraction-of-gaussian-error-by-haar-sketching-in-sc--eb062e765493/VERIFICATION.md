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

# Reproducibility and limits

Execute `python verify.py` using Python 3 and NumPy. With deterministic seed 20261105, direct Haar-QR and Gaussian sketch-and-solve Monte Carlo calculations, independent beta/gamma construction, projector checks, finite-moment formulas and moment-threshold tests produced `VERIFIER_OK 610`. For example, for real \(n=8,\ell=5\), empirical two-sample Kolmogorov distances between direct and factorized samples were 0.0214 (Haar) and 0.0204 (Gaussian), on 2800 direct samples each. For complex \(n=6,\ell=3\), the corresponding distances were 0.0325 and 0.0275.

The random draws are diagnostics, not proofs of equality in distribution, infinitely many cases, strict stochastic order at every threshold, divergence of critical moments, or an asymptotic tail constant. Each assertion requiring an infinite quantifier follows from the invariant-projector and beta–gamma proof in `RESULT.md`.
