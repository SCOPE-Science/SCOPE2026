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

## Reproduction
Run `python3 checker.py` with Python 3.11 or newer and no nonstandard dependencies. The script checks the exact rational four-point alias, positivity of its competitor parameters, the fifth-point curvature separation, the explicit numerical lower bound, and 12,000 supplementary randomly sampled parameter combinations. The mathematical universality of the claim rests on the symbolic proof in RESULT.md, including the composition-derivative inequality and central-difference integral identity; finite numeric sampling is not exhaustive.

## Observational limits
The discrimination is exact for noiseless, equally spaced positive concentration curves of precisely the two defined classes. It is not an empirical goodness-of-fit procedure and offers no uniform measurement-error robustness near degenerate parameter limits. No independent external validation or audit has been performed.
