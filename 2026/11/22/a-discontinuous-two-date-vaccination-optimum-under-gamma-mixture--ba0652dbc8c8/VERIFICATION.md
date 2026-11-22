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

# Reproducibility and boundaries

Run `python3 VERIFY.py` with standard Python 3; no external dependencies or data files are required. On the assembled candidate, the checker printed `PASS 5199 assertions` and a crossover near `350.480179989952`. The verification performs 401 evenly spaced parameter checks, root bracketing and residual checks, exact-formula identity checks, boundary comparisons, and an independent survival-probability interpretation.

The three-root theorem, universal quantifiers, unique switching amplitude and timing jump rely on the exact differentiation, Rolle zero-counting argument, endpoint inequalities and strictly positive envelope derivative in `RESULT.md`; finite diagnostic assertions alone cannot prove those statements. Numerical roots are descriptive only. Nonlinear SIR transmission, correlated exposures, immunity build-up delay and realistic vaccine efficacy are outside scope. No external independent audit or human certification is claimed.
