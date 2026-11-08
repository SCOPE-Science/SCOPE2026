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

The analytical argument and exact quantifiers are in `RESULT.md`. The standalone standard-library checker `CHECK.py` was executed using Python 3 and returned `MATRIX_MODULE_ROWS_EXACT_OK 70357` before packaging. It verifies the finite diagonal-symbol row-mode multiplicity, rank/threshold counts and exact rational energy inequalities in bounded dimensions; these finite assertions do **not** establish the general theorem. The proof of the four infinite-dimensional s-number lower bounds uses complemented row spaces and the quotient norm, independently of this checker. The module-rank-one identity is an explicit polar square-root calculation. Every nonfinite-dimensional component is handled analytically, not by finite enumeration.

The status above concerns only absence of an independent audit. No independent verification or certification is claimed.
