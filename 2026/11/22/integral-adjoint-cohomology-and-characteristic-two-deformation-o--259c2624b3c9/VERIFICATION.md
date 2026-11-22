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

# Reproducible checks and limits

The bundled `checks/verify.py` runs with Python 3, with no external packages. It constructs the integral six-dimensional bracket, checks Jacobi on every independent basis triple, writes all six alternating adjoint Chevalley–Eilenberg matrices over the integers, checks each matrix composition is zero, and computes Smith diagonals using invertible integer swaps, additions, and sign changes. Every pivot and remainder is checked exactly. It confirms six ranks and multiplicities of invariant factors \(1\) and \(2\), the integral torsion tuple, and the all-degree characteristic-two Betti vector.

The program also checks closure and non-boundary of the cocycle \(\phi(x,y)=h+t\) in characteristic two, and directly checks Jacobi and derived-space dimensions for the undeformed and nonzero deformed brackets over \(\mathbb F_2\). The all-field deformation proof rests on the symbolic centrality and quadratic-obstruction argument in RESULT.md, not on finite-field sampling.

The successful certificate prints `TORAL_SL2_INTEGRAL_ADJOINT_COHOMOLOGY_OK`. The review is same-model only; no independent audit, external formal proof, or restricted-cohomology calculation is represented.
