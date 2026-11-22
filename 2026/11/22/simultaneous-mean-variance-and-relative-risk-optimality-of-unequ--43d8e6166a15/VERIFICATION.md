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

# Verification and reproducibility

The standalone `verification.py` runs with Python 3 and SymPy: `python verification.py`. It checks exact symbolic reconstruction of the four conditional mean generator equations, four second-moment equations and mixed incoming absorption conditions; it verifies the uniform-gap integrated second moment, variance and dimensionless derivative identities. It also implements a separate event-driven sampler to compare 240,000 sample paths against those same analytic mean and variance formulas at a zero-rate allocation, two unequal positive allocations, and the balanced allocation.

The deterministic invocation completed successfully and reported 10 symbolic identities, eight generator identities, two algebraic risk identities and 240,000 event-driven trajectories. Numerical tolerances apply only to the Monte Carlo diagnostics. The proof in `RESULT.md` supplies the infinite-parameter and boundary conclusions, including the strict positivity of the derivatives. No independent scientific audit has been performed, and no formal proof-assistant certification is claimed.
