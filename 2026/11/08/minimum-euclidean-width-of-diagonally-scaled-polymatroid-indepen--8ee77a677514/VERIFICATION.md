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

# Verification details

The exact theorem is proved by the greedy support-function identity, the weighted layer-cake Euclidean triangle inequality, and equality rigidity. No external formal certificate or independent audit is claimed.

Run `python3 verify.py` in the same directory with Python 3 and the standard library. Its fixed seed builds 126 small positive singleton-capacity profiles, from coverage functions, binary linear matroids, and partition matroids. It checks each submodular inequality using integer arithmetic, computes the candidate minimum over every nonempty support, checks equality of each predicted minimizing normal with the support-function width, and compares 15,120 additional random unit normals against the sharp value. For unscaled uniform matroids, it compares direct finite support enumeration with \(\min\{1,r/\sqrt n\}\) for bounded tested cases.

Observed output:

`POLYMATROID_WIDTH_FINITE_CHECKS_PASSED profiles= 126 critical_sets= 160 random_normals= 15120`

The tests are finite, floating point for widths and normalizations, and not exhaustive over all real directions or all polymatroids. The analytical proof handles the universal quantifiers and equality cases. Independent audit: not performed.
