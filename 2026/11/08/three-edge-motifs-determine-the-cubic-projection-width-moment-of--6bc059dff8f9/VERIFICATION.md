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

# Verification and reproducibility

To replay the numerical diagnostics, run `python3 verify.py` using Python 3 with its standard library. Successful execution prints `GRAPHICAL_ZONOTOPE_THIRD_WIDTH_MOMENT_CHECKS_PASSED` and the negative prism-minus-biclique cubic-moment difference.

The checker uses deterministic midpoint quadrature of the one-dimensional normal star and path product kernels, checks the analytic triangle value, verifies the independent combinatorial counts of distinct three-edge subsets across all simple graphs with 3–5 vertices, and confirms that the prism and \(K_{3,3}\) have the same first two spherical width moments but different third centered moments.

The mathematical proof is given in `RESULT.md`: the exact spherical normalization, five joint-cumulant kernels, and a complete classification of connected three-edge edge-subsets suffice for all finite connected simple graphs. The computations test implementation and selected instances; they do not certify the universal theorem or historical priority. Independent audit has not been performed.
