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

# Verification

The proof is deductive. It uses the exact two-compartment Laplace transfer function, the strictly positive two-mode variance, a two-pole recurrence, the negative convolution derivative of aqueous response with respect to selective loss, an explicit positive one-condition ambiguity interval, and invariance of domain for the four-reading lower bound. No discrete parameter sweep can replace the universal claims.

The standalone `verify.py` uses `mpmath` precision 70 and a fixed random seed. It checks 150 randomly generated positive parameter quadruples at positive random sample intervals, an independent exact-response reconstruction, positivity of the one-condition fiber, its complete response equality at sampled times, sensitivity to the changed intervention, and monotonicity in the relevant invariant. The executable reported `NUMERICAL_ASSERTIONS_PASSED 2250` and recovered the representative parameters exactly to the stated high-precision numerical tolerance. Execute `python verify.py` with the dependency in `requirements.txt`. A computer execution does not establish independent validation of the mathematical result.

No tests under noisy, censored, unknown-gain, irregularly initialized, spatially advected, nonlinear, or partially selective physical conditions have been performed. Analytic identifiability does not imply a well-conditioned practical inverse; the discriminant and variance can become very small, and the bisection step can be sensitive to data errors.
