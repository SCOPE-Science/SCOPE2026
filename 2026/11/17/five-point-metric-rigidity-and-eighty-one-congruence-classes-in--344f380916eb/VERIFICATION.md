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

Use `python3 verify.py` in a directory containing `orbit_catalogue.tsv`. It requires only the Python 3 standard library and runs with exact integer arithmetic. The checker was executed on the submitted source files, with output:

`24_CELL_FIVE_POINT_METRIC_RIGIDITY_PASSED group=1152 sets=42504 orbits=81 spanning=49 degenerate=32 distinct_signatures=81 burnside_sum=93312 strong_extension=81`

The enumerator forms the complete 1,152-element group from five explicit orthogonal generators; checks every group operation preserves every squared pair-distance; enumerates all 42,504 five-element subsets exactly once in disjoint group orbits; and computes one canonical ten-entry metric signature per orbit using 120 permutations. The 81 signatures are distinct. It independently enumerates all distance-preserving self-permutations of each representative and all permutations induced by setwise-stabilizing group elements; the two sets agree in each of the 81 cases. It verifies the group-action kernel when representatives are dependent and cross-checks the 81 orbit count using Burnside's fixed-subset coefficient formula.

The script checks the 81-row `orbit_catalogue.tsv` byte-for-byte against regenerated output. This is a finite exact executable certificate, not a floating-point experiment or an independently reviewed formal proof. Its coverage is exactly five-element vertex subsets of the regular four-dimensional 24-cell; no assertions for larger subsets are inferred. The published determinant census has been credited as prior work rather than counted as a new discovery.
