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

# Verification of the geometric extremal statement

The checker's public entry point is `python check_unicyclic_surface.py`; it requires Python 3, NetworkX, NumPy, and SciPy. Successful output starts with `UNICYCLIC_GRAPHICAL_ZONOTOPE_FIRST_TWO_SURFACE_LEVELS_PASSED`.

The checker generates all isomorphism types of simple connected unicyclic graphs on four through nine vertices by adding one nonedge to each nonisomorphic tree. The respective class counts are \(2,5,13,33,89,240\). It independently computes areas from (i) all connected bipartitions using spanning-tree weights and (ii) the bridge/cycle-pair formula, then sorts and confirms the smallest two values and their uniqueness. For small cases through order six, it also constructs original graph-root zonotope points, projects to an orthonormal basis of the coordinate-sum-zero hyperplane, and verifies independent convex-hull Euclidean surface areas. All such tests completed without an assertion failure.

The independent convex-hull calculation is deliberately limited to small dimensions because vertex enumeration grows exponentially. Floating-point comparisons use numerical tolerances, not exact symbolic certificates. The all-dimensional conclusions rely on the separate analytical proof in RESULT.md: Euclidean graph-zonotope facet volume, minimal-bond classification, cycle-length separation, strict-concavity/bridge penalty, and majorization. The verification does not constitute external or independent mathematical audit.
