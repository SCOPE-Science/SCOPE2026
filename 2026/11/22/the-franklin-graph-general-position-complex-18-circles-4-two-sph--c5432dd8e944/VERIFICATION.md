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

# Reproducible checks

Run `python3 verify_franklin_gp.py` with Python 3 and no external packages. It checks the exact twelve-vertex graph from its edge formula, all 4096 subsets, each of the 144 forbidden geodesic triples, and its six-dimensional face-vector list. Each of the 56 simplicial collapse pairs is checked for a unique active coface. Every one of the 28 subsequent CW-generator eliminations is performed on freely reduced boundary words; the program asserts that the four remaining relators are empty.

Automorphism backtracking checks all 48 graph symmetries, signed orbits of simplices and rational invariant boundary ranks. The reduced quotient Betti ranks are checked degree by degree. The certificate is exhaustive for the fixed graph and its symmetry group, not a proof of a larger infinite graph-family statement.

Independent external mathematical validation has not been performed; no assertion about the quotient's integral homotopy type is made.
