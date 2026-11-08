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

The included `checker.py` tests the stated analytic covariance formula against a two-state backward matrix semigroup at 1,080 parameter-lag combinations and checks the stationary characteristic transform using a separate matrix-resolvent calculation at nine parameter-wavenumber combinations. It also performs exact-event simulations from 100,000 samples of the stationary last-reset-age law for each of three reversal probabilities. Future Brownian increments are integrated out conditionally in the Monte Carlo covariance estimator, reducing variance without changing its expectation.

These finite diagnostics were run and passed in the same package. Their tolerances and pseudorandom seed are visible in the checker. The proof in `RESULT.md` supplies the all-parameter, all-lag covariance identity, strict order, spectral threshold, and integrated covariance; neither the simulations nor the finite grid are infinite proofs. In particular, this verification does not establish publication priority or independent expert validation.
