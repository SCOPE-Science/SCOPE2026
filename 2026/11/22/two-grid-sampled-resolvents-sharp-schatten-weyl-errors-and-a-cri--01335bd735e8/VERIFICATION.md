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

The included `verify.py` is a standalone Python 3 numerical diagnostic with only standard-library dependencies. It checks equality between sampled scalar and hyperbolic-sine symbols, positivity, cancellation at small argument, a spectral cutoff for the interval Dirichlet generator, and numerical approach of the normalized trace to the exact zeta coefficient. Run `python3 verify.py` from the package root.

These finite calculations are supplementary. The Weyl counting assumption, singular-value tail, uniform spectral truncation and weak-ideal conclusion are proved analytically in `RESULT.md`, not inferred from this diagnostic. The diagnostic does not inspect abstract operators or certify bibliographic novelty. Independent audit is not yet performed.
