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

# Reproducibility and verification scope

Run `python verify.py` with NumPy, SciPy, and SymPy. The script constructs exact labeled and permutation-reduced finite continuous-time generators, exact rational stationary measures, the unforced dual occupation/hitting linear equations, and separately built banded and sparse finite-size solvers. It checks the full-to-reduced marginal identities, the exact source-to-hub graphical duality hitting identity, the stationary ordinary-leaf balance, and residuals of the two-function critical generator potential. A completed replay passed 268 assertions. These checks are independent implementations of the finite models and formulas but do not constitute an independent scientific audit.

The infinite-size conclusion depends on the all-size extinction block estimate, the uniform Taylor-generator bound, Harris graphical duality, and stationary generator balance proved in `RESULT.md`. Numerical trends or finite rational enumeration alone do not establish the asymptotic theorem. The source's historical-priority comparison remains provisional because one potentially relevant paper could be accessed only at abstract level.
