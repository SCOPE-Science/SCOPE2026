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

# Verification of the Petersen spectral-volume result

The standalone verifier `artifacts/verify.py` uses only Python 3 standard-library operations on integers. Running `python3 artifacts/verify.py` checks \(BZ=0\), \(\det(Z^{\mathsf T}Z)=162\), \(\det(BB^{\mathsf T})=648\), and the spectral vertex centroid; it reconstructs each of the \(22\) facets by exact hyperplane tests over the \(252\) candidate five-vertex sets and checks against the independently listed fractional-matching support types. It constructs exactly \(42\) pairwise distinct selected star-cones and checks their \(\pm1\) integer determinants and the complementary \(\pm2\) unsigned-incidence determinants. It prints `PETERSEN_EIGENPOLYTOPE_42_UNIMODULAR_PYRAMIDS_PASS` on success.

The all-facet verification is exhaustive for this fixed ten-vertex object, not a sample. Disjointness and completeness of the circuit-facet triangulation are proved in RESULT.md, not inferred from determinant checks. The algorithm does not assess historical priority, and no external expert or independent audit has been performed.
