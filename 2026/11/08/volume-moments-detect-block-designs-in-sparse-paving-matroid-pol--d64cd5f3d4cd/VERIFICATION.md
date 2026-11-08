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

The proof uses an exact disjoint-cap decomposition of the hypersimplex and elementary Dirichlet integration; no numerical result is promoted into a universal statement. The executable `checker.py` independently triangulates the actual basis-indicator convex hulls using SciPy, computes all simplex integrals with integer determinants and exact fractions using SymPy, and compares the normalized volume, full centroid, and every covariance entry with the formulas. It also verifies special design cases and the strict algebraic sign identity for the codegree coefficient. Use `python checker.py` with Python 3, NumPy, SciPy and SymPy installed. Triangulation construction uses floating-point geometry, but every nonzero simplex contribution is verified by exact integer determinants. An independent audit has not been performed.
