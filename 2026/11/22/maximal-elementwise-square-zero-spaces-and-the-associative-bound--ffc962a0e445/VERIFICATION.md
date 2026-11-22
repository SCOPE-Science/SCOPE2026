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

# Verification record

The mathematical statement is derived from an explicit split quadratic form on the augmentation ideal of an exterior algebra, together with exact classification by \((U,\beta)\). Its algebraic product criterion is verified symbolically in the proof and does not depend on finite tests.

To reproduce the finite-field checks, run `python3 artifacts/check.py` with standard Python 3 from the extracted package root, and compare stdout to `artifacts/check_output.txt`. The tests reconstruct the explicit \((U,\beta)\) families, check individual squares and mixed polarizations, calculate product ranks and closure, and exhaustively compare intersections. The \(\mathbb F_3\) experiment separately loops over all 33,880 three-dimensional subspaces of the six-dimensional hyperbolic ambient space, recovering precisely the 80 predicted maximal isotropic subspaces; the \(\mathbb F_5\) experiment constructs all predicted spaces but does not exhaust every ambient three-subspace.

No finite experiment is offered as an infinite proof, and no external independent audit has been performed. The classical Klein-quadric geometry and the existing Grassmann-algebra literature are explicitly acknowledged in the result.
