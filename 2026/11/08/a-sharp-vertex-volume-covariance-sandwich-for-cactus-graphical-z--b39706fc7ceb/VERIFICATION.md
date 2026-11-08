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

The standalone `artifacts/verify.py` uses only the Python standard library and exact `fractions.Fraction` arithmetic. Replay from the package root with `python3 artifacts/verify.py`.

Its direct acyclic-orientation enumeration covers thirteen connected cacti, including single cycles, bridges, two-cycle attachments, and three-cycle attachments. It constructs all distinct graphical-zonotope vertices and checks exact covariance entries. An independent parameterization of equal-volume parallelotope tiles computes volume second moments, which are checked against the claimed coefficients. Rational Laplacian cofactors test the determinant product on each example. The checker also confirms the formulas for local weight ratios for cycle lengths 3 through 150 and records the noncactus boundary case of the complete bipartite graph with parts of sizes two and three.

Observed successful output:

`CACTUS_VERTEX_VOLUME_COVARIANCE_CHECKS_PASSED profiles=13 vertices=2318 matrix_entries=900 cycle_lengths=148`

These finite computations are corroborative. The universal inequalities, equality conditions, and determinant ratio are proved analytically in `RESULT.md`. Independent audit has not been performed.
