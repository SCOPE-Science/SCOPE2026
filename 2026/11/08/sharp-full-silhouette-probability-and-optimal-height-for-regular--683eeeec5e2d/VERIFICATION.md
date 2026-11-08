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

# Reproducibility and limits

The exact probability follows from the facet-normal sign pattern, the scalar-product normal-cone test, the centered Gaussian triple-sign identity, and inclusion-exclusion of three successive side normals. The optimizing height follows by differentiating an arcsine difference and comparing positive radicals. The large-\(n\) limits follow from a uniform fifth-order remainder for an arcsine/Taylor expansion near the relevant shape parameter.

Run `python3 verify.py` from the same directory. Requires Python 3 with NumPy, SciPy and mpmath; the checker uses a fixed random seed. It constructs literal projected two-dimensional convex hulls of regular polygonal pyramids (rather than using the normal-sign event formula), compares frequencies with exact probabilities for 12 pairs of side-count/height parameters, checks the optimizer locally and the critical identity, and verifies the asymptotic constant using arbitrary precision. A successful run prints `ALL_REGULAR_PYRAMID_FULL_SHADOW_CHECKS_PASSED`.

Finite Monte Carlo, finite precision, and the particular sample sizes are not exhaustive checks or proofs for all integers and heights. The analytical argument in RESULT.md supplies the universal quantifiers. Historical priority has not been independently established; the four-sided-base case belongs to prior published work and is excluded. Independent audit: not performed.
