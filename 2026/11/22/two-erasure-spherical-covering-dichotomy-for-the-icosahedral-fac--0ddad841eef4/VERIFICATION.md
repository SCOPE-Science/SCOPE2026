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

# Verification and exact-scope limits

The standard-library `verify.py` runs with Python 3.9+ and no third-party packages. It reconstructs both icosahedral coordinate orbits using rational intervals around square roots built with `math.isqrt`; each strict sign test is an exact rational comparison of certified enclosing intervals, not a floating-point heuristic. It verifies all sixty original supporting triangular faces and their strict noncontact gaps. For a representative incident two-erasure it verifies all three additional polygonal support planes against all retained vertices, the 51 inherited facets, 82 boundary edges in 54 faces, double incidence of each edge and connected Euler characteristic two. It tests the exact Gram determinant formulas and strict height inequalities; face coplanarity is separately established by the algebraic identities in `RESULT.md`. It also verifies the 60/180 incident/nonincident mixed-pair counts and the nonincidence cap-separation inequality.

Observed output: PASS with original covering cosine approximately 0.922602194544, ordinary two-erasure cosine approximately 0.794654472292, exceptional cosine approximately 0.768858636429, and intermediate new-facet cosine approximately 0.828263486752. No Monte Carlo result is used as proof. The supporting-plane and combinatorial proof applies to all 496 deletions through symmetry and geometric inequalities. Historical priority is provisional. Independent audit has not been performed.
