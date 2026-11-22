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

All results use the finite spin-plus-bath generator defined in `RESULT.md`. Run `python verify.py` (requires SymPy) to reconstruct the symbolic orbit law and independently compare it against full 32-state generators evaluated at three exact rational parameter pairs. The exact algebraic factorization, asymptotic coefficients, stationary normalization, and orbit multiplicities are checked. The printed success message is `PASS: all exact mathematical checks`.

This checker does not establish that the claim has not appeared in unindexed publications. The positivity proof uses explicit polynomial coefficients and is not inferred from numerical tests. Mathematical claims are reviewed within this package; independent audit has not been performed.
