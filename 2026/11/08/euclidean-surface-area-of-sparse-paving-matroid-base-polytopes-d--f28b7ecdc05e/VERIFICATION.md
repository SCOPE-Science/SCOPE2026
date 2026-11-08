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

# Verification of the Euclidean boundary-area law

The proof uses explicit Euclidean rather than lattice-normalized facet measures. It derives hypersimplex baseline area using Eulerian numbers, computes the new Cartesian-product facet, computes removed old-facet pyramids in the correct facet-affine metric, proves disjointness of strict excised corners, and proves sharp positivity/rank monotonicity.

`check_surface.py` requires Python 3, NumPy, and SciPy. Execute `python check_surface.py` next to this file. In an execution of the actual embedded source the output was `SPARSE_PAVING_EUCLIDEAN_AREA_CHECKS_PASSED 73 and_rank_profiles 76`. The checker constructs incidence-vector convex hulls in an orthonormal basis and compares their intrinsic Euclidean surface areas with the closed formula. The finite runs are supplementary and do not establish the all-parameter theorem.

Checks do not cover disconnected matroids, arbitrary affine changes of coordinates, or literature priority; an independent audit was not performed.
