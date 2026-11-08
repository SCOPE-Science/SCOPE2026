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

# Reproducibility and boundaries

Run `python check_type_b_incenters.py` with NumPy and SciPy. The program independently computes inclusion-maximal independent sets; checks the stated affine-dimension bound over the full Prüfer-sequence census of all \(18{,}248\) labeled trees of orders two through seven; verifies odd-path crosspolytope support functions with linear programming in dimensions up to ten; checks seven even-order extremal tree constructions; and independently compares the polar signed stable-set vertices and the direct convex-hull primal facet distances in small graph samples.

The executed checker terminated successfully with `TYPE_B_INCENTER_CHECKS_PASSED trees 18248 convexhull_facets 362 paths 9 extremizers 7`. Its floating-point facet distances and LP computations use numerical tolerances and support, but do not prove, exact universal statements. Every infinite-range conclusion is proved algebraically and combinatorially in `RESULT.md`; no independent mathematical audit has been performed.
