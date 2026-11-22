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

The analytical proof is self-contained in `RESULT.md`. The standalone `verify.py` checks the exact quotient formula and the 10-vertex graph adjacency, symbolically differentiates the principal eigenvalue, confirms the exact threshold polynomial, and compares the matrix spectral radius with the equitable quotient at both crossings and at the optimal and extreme commuter fractions. The script requires Python 3, SymPy, and NumPy; invoke `python verify.py` in the directory containing this document.

The source model is the published fixed-information-equilibrium linearization; the claims are restricted to linear invasion of the disease-free state, with the information equilibrium itself stable. The full coupled nonlinear stochastic epidemic is not certified. Finite checks are supplementary, not proofs for arbitrary graph size or parameters. The critical equality cases have a unit multiplier and remain unclassified nonlinearly. No independent scientific validation has been performed.
