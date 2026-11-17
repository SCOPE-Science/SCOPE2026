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

# Reproducible verification

Run `python halfcube_ridge_verify.py` with NumPy and SciPy installed. The checker enumerates all even-parity vertices in dimensions \(n=4,5,6,7\), constructs all coordinate and odd-corner simplex facet supporting inequalities, and independently computes Euclidean affine volumes from singular-value orthonormal coordinates and convex hulls.

Its all-pairs facet-intersection test verifies that only the two claimed ridge types appear, reproduces their actual counts, measures, exterior angles, and the aggregate normalized \(V_{n-2}\). The volume of the polytope itself and each facet is also checked by direct convex-hull integration against the formulas. The final output is `HALFCUBE_STEINER_PASS`.

These are exhaustive computations within the listed dimensions, not an exhaustive all-dimensional proof. The analytic argument in `RESULT.md` establishes the general case by facet intersection and the polyhedral Steiner face-angle identity. Python's floating-point comparison tolerance is \(10^{-7}\) for volumes and angles; the categorical ridge-count equality is exact over enumerated integer coordinate sets. No independent mathematical audit has been performed.
