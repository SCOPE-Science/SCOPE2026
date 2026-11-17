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

# Verification and limits

The analytic proof uses exact polar coordinates for a regular polygon, an explicit radial boundary Taylor polynomial, the exact Euclidean cosine rule and the exact polygon area. The compact localization argument and the fact that the derivative of the squared positive part is Lipschitz provide a uniform integrated remainder, including at the parity onsets. The local onset constants are exact quadrant integrals. The conditional law follows from density convergence on the limiting four-dimensional polytope-like region.

The accompanying `verify_area_polygon_crossover.py`, run with numpy and scipy as specified in `requirements.txt`, independently evaluates the two crossover integrals using Gauss–Legendre quadrature and the exact four-dimensional polygon distance event by deterministic Sobol integration. It completed `AREA_POLYGON_PARITY_TWO_TERM_OK comparisons=8`. The tested odd and even polygon sizes were 31, 32, 63, 64, each at rescaled thresholds 3 and 8. All eight corrected predictions were closer to exact-geometry numerical estimates than the leading profile. The script also checks the parity thresholds, two quartic onset coefficients and disk envelope.

Finite numerical integration supports the proof but does not establish uniform convergence, original historical priority, or independent validation. The quoted remainder is uniform only on each bounded rescaled-threshold interval, and the result does not apply to arclength-uniform boundary sampling.
