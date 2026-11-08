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

# Analytic and computational verification

The unit-sphere area-normalized probability is computed using a two-point spherical geodesic change of variables and two elementary integrals. The analytic derivation proves the continuum identity; simulations are not substituted for a proof.

The standalone `check.py` implements two independent numerical checks: (i) deterministic Simpson quadrature of the conditional great-circle integral, using a boundary-regularizing substitution; (ii) direct surface-area-uniform sampling of both endpoints and computation of the minimum South/North coordinate over their actual minimizing great-circle arc, without using the integral formula to classify successes. The random generator is seeded, so the displayed check is reproducible.

Observed successful samples at six excluded-cap radii had absolute deviations within the specified five-standard-error threshold; the integral agreed with the cubic formula to its prescribed tolerance. The exact maximum check also succeeded. Run `python3 check.py`, requiring only Python's standard library, to repeat it. The checker prints `SPHERICAL_CAP_SHARP_GEODESIC_NONCONVEXITY_OK` on success.

The comparison literature consists of primary full texts from Santaló (1946) and Lassak (2013 online), along with an abstract-only comparison for Le (1989). No independent review or historical priority certification has been performed; unindexed sources remain a risk.
