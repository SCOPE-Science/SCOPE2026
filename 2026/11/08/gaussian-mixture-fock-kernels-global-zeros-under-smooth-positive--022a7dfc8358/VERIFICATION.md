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

# Finite reproducibility checks

Run `python CHECK.py` with a standard Python interpreter. The script has no third-party dependencies. It checks exact rational Gaussian moments, the agreement of two independently derived kernel expansions on several complex arguments, real-root bracketing of the normalized exponential series for several small positive mixture parameters, the size of the first displacement, and a grid of positive-curvature inequalities.

The main infinite-zero theorem follows instead from the exact growth and coefficient asymptotics plus finite-zero Hadamard factorization. The sharp first-zero escape follows from a half-plane exclusion and a Rouché argument near the two-exponential cancellation point. Uniform smoothness and positive curvature follow from a radial Hessian identity and a global Gaussian supremum bound. No computer search, finite truncation, or assertion count is presented as an infinite proof or external certificate.

The exact norm normalization is included in the theorem. The negative logarithm of a probability density differs from the displayed potential by an additive constant only; this does not affect its Hessian or uniform convergence after fixing that normalization. Near-diagonal lower bounds in the motivating literature do not imply global zero-freeness.
