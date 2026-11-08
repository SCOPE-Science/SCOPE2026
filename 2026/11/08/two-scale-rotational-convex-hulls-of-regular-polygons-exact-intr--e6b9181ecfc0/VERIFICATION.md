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

# Reproducibility and claim-to-evidence

The stated formulas concern a Euclidean convex hull of two concentric regular polygons with identical side counts. The proof in RESULT.md uses a supporting-edge containment criterion, an alternating-vertex argument, polygon shoelace/chord sums, and an exact trigonometric factorization proving the perimeter derivative is positive whenever the inner polygon protrudes. The two gain exponents follow from a Taylor expansion of explicit formulas, not from extrapolation.

Execute `python VERIFY.py` with Python 3, NumPy and SciPy available. The implementation constructs the input points independently, invokes SciPy's two-dimensional ConvexHull routine for its area and perimeter, and compares with the closed forms at 10,619 combinations: 37 side counts, seven representative scale ratios each (including threshold-adjacent cases), and 41 orientations. The expected message is `ROTATIONAL_HULL_PROFILE_TESTS 10619 active 4436 inactive 6183 failures 0`. Numeric values are checked within absolute error \(2\times10^{-7}\); this is evidence for the formulas, not an exhaustive proof over continuous parameters.

The scope does not include unequal side counts, off-center polygons, affine distortions, or higher-dimensional convex hulls. Earlier results about translated hulls and nonconvex unions are not applied as substitute proofs. The independent audit remains unperformed.
