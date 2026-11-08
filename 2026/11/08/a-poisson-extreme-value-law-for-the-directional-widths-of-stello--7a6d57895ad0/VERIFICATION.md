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
# Reproduction and scope

The standalone file `verify_stellohedron.py` runs with Python 3, NumPy and SciPy and is intentionally independent of any external files. It checks exact finite support identities against direct subset enumeration, the Gaussian one-dimensional mean-width integral against separate normal-direction sampling, the trigamma summation against the dilogarithm expression, the exponential-arrival representation against its exact first two moments, and sample-size normalization at several dimensions. Expected terminal marker: `STELLOHEDRON_WIDTH_POISSON_LIMIT_CHECKS_PASSED`.

This finite testing does not establish a weak limit, moment convergence, historical priority, or external mathematical certification. The analytical proof is in `RESULT.md`, particularly the Bernoulli-thinning truncation step and the two-tail Gaussian Poisson limit.
