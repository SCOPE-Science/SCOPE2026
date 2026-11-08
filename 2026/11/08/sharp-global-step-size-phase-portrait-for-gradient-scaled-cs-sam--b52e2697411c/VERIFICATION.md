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

## Reproducibility and limits
Run `python3 CHECK.py` with Python 3 standard library. The standalone checker compares the original two-stage update with the rational reduction using exact fractions, verifies the rational symmetric two-cycle, and tests the strict monotonicity identities, sample attraction inequalities and a long critical trajectory. Expected output: `PASS: 11865 supplementary checks; rational two-cycle and critical-rate test verified`.

The global statements are proved by the derivative signs, exact radial comparison inequalities and reciprocal-amplitude asymptotics in `RESULT.md`, not by finite sampling. Exact-arithmetic verification does not validate floating-point implementations or extend the theorem to multidimensional or stochastic problems. Independent mathematical audit has not been performed.
