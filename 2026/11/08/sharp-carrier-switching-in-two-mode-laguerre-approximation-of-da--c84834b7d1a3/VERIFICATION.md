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

## Direct checks
The independent numerical integration of the first two Laguerre inner products agrees with the simplified rational projection formula for several frequencies and scales. Symbolic algebra verifies the exact difference factorization, the derivative polynomial, the discriminant, and the two nonzero optimum levels at the transition. Direct global frequency grids and scalar optimization confirm representative regimes. Running `python CHECK.py` prints `TWO_MODE_LAGUERRE_CARRIER_EXACT_AND_INTEGRAL_CHECKS_PASSED`.

## Mathematical boundaries
The global optimizer classification for the full continuous carrier domain is proved analytically by sign and convexity arguments. The finite sampling check is corroborative only. Projection uses ideal infinite-half-line integrals; numerical quadrature, regularized inverse methods, modified scales, and frequencies below \(\omega=2a\) are outside the theorem. Publication-priority checking is not an independent audit or exhaustive guarantee.
