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

The mathematical proof in `RESULT.md` is self-contained for the asserted fixed-order asymptotic and rests on an exact deck-image comparison, an antiperiodic Fourier trace identity, explicit vertical moments and a controlled perturbation-by-edge expansion. It distinguishes the intrinsic orientation character of a closed loop from a representative-dependent open-edge parity.

Run `python3 verify.py` with Python's standard library. The script verifies 600 direct deck-image minimizations; evaluates the trace coefficients for powers two through six (with finite-series truncation tolerance); checks the single-edge quadratic response for polygon sizes four, five and six; and draws 180,000 polygons in each of seven configurations, totalling 1,260,000 sampled geodesic polygons.

The observed proportions at horizontal-to-vertical aspect ratios one and two, respectively, were: four-vertex polygons 0.342050 and 0.333306; five-vertex polygons 0.401956 and 0.395106; six-vertex polygons 0.438233 and 0.436906. The four-vertex aspect-four sample gave 0.332578. These values are consistent with the displayed asymptotics within declared finite-sampling tolerances, but the asymptotic error for aspect ratio one is not neglected. Completion marker: `KLEIN_ALL_POLYGON_PARITY_QUARTIC_OK`.

A numerical series truncation cannot certify an infinite trace identity, and Monte Carlo cannot certify the expansion's remainder. The proof, not the checker, establishes those assertions. Historical priority is provisional; independent audit has not been performed.
