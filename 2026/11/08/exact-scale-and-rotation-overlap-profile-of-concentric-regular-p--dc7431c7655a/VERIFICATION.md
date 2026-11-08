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
# Verification notes

The proof uses explicit halfplane representations of two regular polygons, one exposed small vertex per outer supporting line, and disjoint clipping triangles. Its exact area formula is differentiable on each branch, permitting direct derivative and Taylor checks. At equal scales the one-sided derivative must be taken after canceling the shared numerator and denominator factor. At strictly unequal scales the zero-loss plateau ends at a quadratic contact. Circular-arc overlap at each radius supplies an independent route to the radial-weight monotonicity; the strict weighted case follows because the already-proved ordinary area gap must occupy positive radial measure on the active annulus.

Reproduce with `python verify.py` (Python standard library only). The script uses independently built literal polygon vertices, halfplane intersection via Sutherland–Hodgman clipping, and shoelace area, testing 7,200 seeded configurations with polygon orders 3–50 and arbitrary positive scale ratios, and endpoint/phase tests. Observed output: `ALL_OK 7200 max_relative 6.452783596893903e-16` and `PHASE_AND_ENDPOINTS_OK`. This calculation checks geometry and numerical normalization but is not an exhaustive proof of all real parameters.

Mathar's 2013 study covers rotation/containment geometry, and the exact containment threshold alone is not a novelty claim. The newly reviewed formula and accompanying phase transitions concern the restricted same-side-count, centered case; no translations, mixed polygon orders, other dimensions or nonradial measures are covered. Historical priority remains provisional. No independent audit has been performed.
