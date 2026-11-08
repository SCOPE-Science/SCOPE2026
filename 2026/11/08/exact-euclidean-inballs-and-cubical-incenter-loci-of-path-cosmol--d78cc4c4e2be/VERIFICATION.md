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

# Reproducibility

Run `python3 verify.py` in an environment with NumPy and SciPy. The checker constructs the original \(3(n-1)\) vertices and all interval facet normals directly, calculates their Euclidean projections, and verifies the exact double-cover identity.

It solves an independently formulated linear program for all integer path orders from \(4\) to \(11\), verifies 137 specified vertices of the proposed box of incenters (exhaustive corners for \(4\le n\le10\); extreme endpoint configurations at higher orders through \(15\)), and checks that 110 tested interval inequalities define genuine facets of the vertex hull for \(4\le n\le8\). It confirms the computed optimum and every sampled center's containment. The successful output is:

`PATH_COSMOLOGICAL_INBALL_VERIFICATION_PASSED 8 137 110`

These are finite computational tests. The complete proof relies on the facet theorem, the exact double-cover identity, and concavity inequalities, not a claim of computational exhaustiveness in all dimensions. The verification requires no external network and does not constitute independent validation.
