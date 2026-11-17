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

# Reproducibility and verification

Run `python checker.py` in the same directory as this document. Only the Python standard library is used. The program builds every set of four distinct integer nodes for \(N=3\) through \(59\) and checks its six-factor Vandermonde product, the complete maximizing quadruple set, and the analytical gap-balancing and middle-gap predictions. Separate determinant calculations are performed for representative maximizing tetrahedra. It also checks all integer middle-gap candidate comparisons and odd-index Fibonacci resonance indices through \(N=10000\).

Actual output:

`CYCLIC_FEKETE_PASS full_n=4..60 full_quadruples=5949147 1d_N=3..10000 ties=5,13,34,89,233,610,1597,4181 exact_determinants=PASS`

The unrestricted theorem rests on the symbolic adjacent-gap identity, strict inequalities, and Pell descent written in RESULT.md; no finite run establishes the claim for arbitrary \(N\). The only unclassified equality cases are possible nonvertex maximizing tetrahedra inside the polytope. Historical priority is provisional and independent mathematical auditing has not been performed.
