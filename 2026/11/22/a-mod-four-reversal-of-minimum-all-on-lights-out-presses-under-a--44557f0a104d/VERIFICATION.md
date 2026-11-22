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

## Proof-level checks
The proof uses actual graph definitions with no overlapping neighbors for \(n\ge3\), exact elimination of the prism rail, and exact antipodal reduction for the Möbius ladder. In both cases every press solution is forced to be period four, and the original equations are explicitly reimposed to get necessary and sufficient finite-word conditions. The all-on and quiet enumerators come from a complete two-/four-bit case split. The minimum-press claim is the least positive exponent of the all-on polynomial; all solution counts and endpoints are accounted for.

## Independent algorithmic checks
`check_gauss.py` constructs the full binary matrices afresh for \(3\le n\le80\), and computes *all* affine solution vectors by row reduction. This covered 312 pairs of a graph and constant target, checking complete weight multisets. `check_exhaustive.cpp` directly toggles closed neighborhoods along a Gray-code enumeration of *every* press subset for \(3\le n\le11\), in 36 complete census cases. Both scripts passed when executed from their actual packaged source files. These computations are finite corroboration; the all-order theorem depends on the proof in RESULT.md.

## Known coverage and limitations
Existing prism-quiet spectra and Möbius quiet-solution counts are credited, not presented as new claims. No shortest-solution theorem for arbitrary initial light patterns is asserted. Index-based searches cannot rule out unpublished or unindexed prior enumerations. Independent scholarly validation is not claimed.
