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

# Reproducibility and exact scope

The scripts `verify/transfer.py` and `verify/direct.py` were executed with Python 3 (SymPy required only for `verify/transfer.py`), and their complete saved output is in `verify/transfer.out` and `verify/direct.out`. They were replayed from these same concrete source paths, not from historical programs.

`verify/transfer.py` constructs the explicit 81-by-81 integer transfer matrix, factors its characteristic polynomial by exact symbolic computation, compares its power traces with polynomial Newton sums for every integer length 5 through 18, and rejects any discrepancy. `verify/direct.py` independently enumerates every three-state assignment for lengths 5 through 11 (total 265,599 states), applies three synchronous updates to determine initial primitive-three behavior, and compares it with the local successor criterion; it also tests nearest-neighbor rings for lengths 3 through 12.

The finite checks do not constitute an infinite proof. The proof for all lengths uses the exact local equivalence, closed-walk transfer bijection, symbolic determinant identity, and standard trace/eigenvalue identity. The asymptotic error follows from a stated polynomial root bound.

No independent audit has been conducted. The priority comparison was limited by the absence of full text for one older source.
