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

Exact matrix and combinatorial checks are implemented in `verify.py`. Reproduce with Python 3 and SymPy (`python verify.py`). The procedure constructs the weighted 16-state transition matrix from the locally forbidden factors, recomputes the factored characteristic polynomial, and tests the weighted trace against exhaustive independent graph-neighborhood enumeration for every cycle order from 5 through 16. It also checks equivalence of the original graph definitions with forbidden words on every subset in that range, and all coefficient recurrences and extreme sizes through order 39.

Observed output included `EXACT_CHARACTERISTIC_POLYNOMIAL_OK`, twelve `GRAPH_AND_TRANSFER_EXHAUSTIVE_OK` lines, `WEIGHTED_RECURRENCE_AND_SUPPORT_OK 11..39`, and `VERIFY_OK`.

The independent graph checks are finite, not an all-orders certificate. The all-orders proof is the neighborhood characterization and finite-state transfer/characteristic-polynomial argument in `RESULT.md`. No independent human or external mathematical audit is claimed.
