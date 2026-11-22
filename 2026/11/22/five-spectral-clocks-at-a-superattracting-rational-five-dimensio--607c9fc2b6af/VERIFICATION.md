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

Run `python CHECKER.py` with Python 3 and SymPy as declared in `requirements.txt`. It tests the exact Cayley identity, the five-by-five characteristic polynomial, spectral expressions, primitive positivity, representative positive initial histories and small-parameter amplitude sensitivity. A separate high-precision five-mode trial compares the full spectral formula with direct logarithmic iterates at several indices; errors become super-exponentially small. These finite examples verify implementation consistency, not the infinite theorem. The exact spectral decomposition, positivity argument, root isolation and dominated-convergence step are established mathematically in `RESULT.md`.

The initial states are strictly positive and different from one. A zero Cayley coordinate is deliberately outside the theorem. The proof does not rely on direct floating-point subtraction of a state from its superattracting equilibrium.
