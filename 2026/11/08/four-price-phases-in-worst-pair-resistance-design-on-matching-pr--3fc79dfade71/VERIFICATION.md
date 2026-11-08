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

# Verification of the analytic result

Reproduce the supplementary checks using `python verify.py` with Python, SymPy and SciPy.

The standalone checker builds each weighted bipartite graph directly, forms its Laplacian without using the claimed spectral formula, and inverts the reduced Laplacian with rational arithmetic. It compares within-part, matched and unmatched cross-part pair resistances with the stated expressions, including at zero matching conductance. It separately checks the closed price phases against bounded scalar minimization and direct competitor values, and verifies differentiation identities symbolically.

An actual execution passed 144 exact grounded-Laplacian shell checks, 108 phase/optimization cases, and three symbolic derivative identities. The proof of the all-parameter statement is the analytic symmetry reduction, exact spectral decomposition and derivative sign classification given in `RESULT.md`; finite testing does not establish an infinite-parametric claim. No independent mathematical audit has been performed.
