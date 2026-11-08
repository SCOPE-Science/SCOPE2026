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

Run `python check.py` using standard Python 3. The program uses only standard-library exact rational arithmetic and checks representative dimensions, contraction factors, attracting two-cycle identities, two-step contraction and finite-grid first-switch inequalities. At preparation time its output was `PASS 7030 exact-rational supporting assertions`.

The mathematical proof does not depend on simulation. The high-dimensional exponential and lattice limits are established from the exact independent-coordinate order-statistic formula, ceiling continuity away from integer atoms, and bounded rounding error. Numerical finite samples, even at large dimension, cannot prove either limiting law.

The file reports no independent audit. Its verification is local reproducibility plus the accompanying analytical proof.
