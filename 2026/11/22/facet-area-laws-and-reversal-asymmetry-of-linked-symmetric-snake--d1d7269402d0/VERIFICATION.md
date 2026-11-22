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

The companion Python checker computes poset linear-extension counts by subset dynamic programming, independently enumerates all admissible binary vertex assignments, applies the displayed affine map, and uses `scipy.spatial.ConvexHull` to recompute standard-Euclidean volume and total surface area. Requirements for numerical geometry replay: Python 3.10+, NumPy and SciPy; only the Python standard library is needed for exact extension counts and reversal-gap checks.

Completed checks: all \(2^{n-1}\) linked profiles at every \(n=3,4,5,6,7\) (124 profiles) matched Euclidean convex-hull area and volume within \(10^{-6}\). The two endpoint profiles were separately tested by exact extension counts through \(n=12\), and their analytic area-gap formula was checked for positive values in that range. These computations illustrate the formulas and test the implementation; finite checks do not prove the all-\(n\) statement.

The proof in `RESULT.md` supplies the general argument: the affine map is unimodular; all order-polytope facets come from covers and extrema; each facet has an extension-count lattice volume and a primitive-normal covolume; a real-variable inequality proves the strict reversal gap for every dimension in scope.
