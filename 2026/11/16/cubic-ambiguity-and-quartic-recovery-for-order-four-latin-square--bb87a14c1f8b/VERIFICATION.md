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

The two delivered exact-arithmetic scripts were executed on their packaged input `pivot_manifest.json`. The primary generator found 576 fully labelled squares and 54 distinct four-block switch cubes, checked cancellation of all at-most-three-cell assignment events, and found 522 independent columns by degree three and full 576-column independence by degree four over the prime field with five elements. The independent generator constructed the 576 squares by row completion, verified the square-order digest, and checked independence of all 576 selected columns over the prime field with seven elements. It also checked a canonical 16-square alternating cube.

The upper bound at cubic degree is an integer signed-measure construction with 54 independent members, witnessed by private squares. The lower bounds use finite-field nonvanishing minors, which are valid exact rational lower bounds. The checks establish results only for fully labelled order-four Latin squares and no infinite-order extension or conditioning estimate. Reproduction requires Python 3 with NumPy installed.
