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

# Reproducible verification

Run `python3 verification.py` with a standard Python 3 interpreter. No third-party dependencies or downloads are required.

The program performs independent exact polynomial-ring multiplication of the strongly regular adjacency algebra to fourth order, compares its edge and nonedge coefficients with the closed expressions, and confirms the nonedge quadratic discriminant identity symbolically. It then generates 12 concrete graphs, independently checks their strongly regular parameters by common-neighbor counts, and compares all 9,768 entries from sampled exact-rational RK4 matrices with the appropriate formulas. Every checked matrix has exact unit row sums.

The graph instances are Petersen, triangular graphs on 5 and 6 base points, rook graphs on 3-by-3 and 4-by-4 grids, Shrikhande, complete bipartite graphs with part sizes 3 and 4, and Paley graphs of orders 5, 13, 17, and 29. The output must end with both `passed` messages. The inequalities establishing all-dimensional positivity, the uniqueness of the cubic zero, and strict improvement over the forward Euler step are proved algebraically in `RESULT.md`. Finite checks cannot certify arbitrary graph parameters or every real timestep.

A later independent mathematical audit has not been performed.
