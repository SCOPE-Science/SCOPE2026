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

# Verification

The proof uses an all-integer degree-two basis of same-endpoint path differences and a normalization over arbitrary abelian coefficient groups. The identification of first cohomology is functorial in coefficients; the universal coefficient theorem implies absence of integral degree-one torsion.

Execute `python3 verify_hasse_h1.py` using Python 3 standard library. The direct finite checker tests 57 connected pure two-complexes at each of the primes 2, 3 and 1000003, totaling 171 modular consistency checks. It covers the connected facet and vertex-wedge extremes, but cannot certify all finite complexes or the integral torsion conclusion.

Scientific limits: the simplicial complex must be nonempty, pure two-dimensional and connected; return arcs must go from every facet to every vertex. Higher-degree groups and cup products are outside the claim.
