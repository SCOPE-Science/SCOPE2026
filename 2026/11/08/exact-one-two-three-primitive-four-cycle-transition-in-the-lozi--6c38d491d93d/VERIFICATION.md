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

## Checks
The standalone checker recomputes the three formal length-four trajectories symbolically, confirms the algebraic switching-collision identity and unique threshold-polynomial expansion, and independently enumerates the sixteen four-step affine itineraries at twenty rational parameter pairs with exact arithmetic.

Expected successful messages: `EXACT_SYMBOLIC_IDENTITIES_OK`; `FULL_16_ITINERARY_RATIONAL_CENSUS_20_CASES_OK`; `SADDLE_TRACE_CLASSIFICATION_OK`.

## Scope and limits
These finite checks are supporting reproducibility only. The proof establishes the entire real parameter wedge analytically. The boundary count is proved from exact polynomial divisibility rather than numerical sampling. An independent scientific audit has not been performed.
