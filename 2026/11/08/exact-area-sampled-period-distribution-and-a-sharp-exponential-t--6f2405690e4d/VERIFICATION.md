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

# Reproducibility and limits
Run `python scripts/check_period_law.py` with dependencies from `requirements.txt`. It verifies the original-time ODE scaling algebra, exact Hamiltonian identity, independent elliptic quadratures for the quarter-period and for the product density, the elliptic CDF, and sample ratios of exact tails to the displayed two-term expression. It does not establish an infinite limit by numerical sampling; the analytic error terms in `RESULT.md` do that. The original 2024 source was inspected in its full-text arXiv HTML form. A prior published note already states the symmetric elliptic period formula; the new inference is the area-sampled law. Only the present result receives this scientific check. No independent audit has been performed.
