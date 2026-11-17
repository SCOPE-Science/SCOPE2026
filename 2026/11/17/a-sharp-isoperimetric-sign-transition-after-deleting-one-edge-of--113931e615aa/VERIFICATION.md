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

# Reproducibility and scope

Run `python checks/check_one_missing_edge.py` with Python 3, NumPy and SciPy. The program directly constructs standard vertex coordinates, uses orthonormal projection into the intrinsic affine difference space, and compares `scipy.spatial.ConvexHull` volume and boundary-area outputs with the closed formulas for eleven parameter pairs through \((5,5)\). Both independent metric comparisons pass.

For the seven pairs not handled by the uniform analytic inequalities, the program encloses each square root between exact fractions with denominator \(10^{12}\). It then propagates rational intervals through \((1-z\varepsilon)^d-(1-\varepsilon)^{d-1}\), and asserts that the resulting interval excludes zero with the claimed strict sign. It prints `RATIONAL_BOUNDARY_PASS cases=7`. This is an exact finite certificate conditional only on ordinary integer arithmetic, and its whole sign logic is visible in the script.

The infinite range requires the symbolic inequalities in `RESULT.md`. Finite convex-hull tests and seven strict arithmetic enclosures do not by themselves prove those general inequalities or historical novelty. All measures are in the intrinsic standard Euclidean metric, for a product with two factors of size at least two and exactly one deleted corner. No independent mathematical validation has been performed.
