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

# Verification record

The analytic proof uses an exhaustive parity classification of deck translates and exact integration of the pushed-forward arclength law. The standalone file `verify_mobius.py` was executed with Python 3 standard-library dependencies only, returning:

```text
MOBIUS_BOUNDARY_LAW_OK deck_pairs=210000 independent_cdf_checks=68 mean_quadratures=7 inverse_checks=7
```

The checker enumerates nine distinct deck translates for 210,000 random boundary pairs over seven positive aspect-ratio cases, confirms formula (1) to high numerical precision, independently approximates 68 CDF values by 25,000-point midpoint integration, checks seven expected values against a separate 100,000-point quadrature, and checks inverse identification and wide-band invisibility. These are finite checks only; the deck-group proof establishes the infinite family. No independent audit has been performed.
