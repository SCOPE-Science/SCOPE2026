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

# Computational verification

The two different graph presentations agree on all five- and six-vertex seed counts for the 42-vertex \(\operatorname{PG}(2,4)\) incidence graph. The homogeneous-coordinate program tests every set size from one through six; the affine-coordinate program tests every size-five and size-six subset and then the complete exchange graph. Both implement simultaneous unique-unobserved-neighbor forcing, not asynchronous forcing. A successful configuration is counted once as an unordered subset.

Expected certificate values: \(850{,}668\) failed five-subsets, \(5{,}245{,}786\) examined six-subsets, \(566{,}160\) successful six-subsets. The nonzero (point count, observation time) entries are \((2,3):65{,}520\), \((3,2):52{,}080\), \((3,3):383{,}040\), \((4,3):65{,}520\). The minimum-set jump graph has \(19{,}706{,}400\) edges and one component. The slide graph has \(2{,}257{,}920\) edges and 30,241 components (30,240 singletons and one component of 535,920 vertices). Of the singletons, 10,080 have observation time two and 20,160 time three.

Recompile and execute the three supplied C++17 files using the commands in `RESULT.md`. The two connectivity algorithms and distinct coordinate geometries form a reproducible computational cross-check, not an independent mathematical audit. A graph of order beyond four is not tested, and no untested generalization is asserted.
