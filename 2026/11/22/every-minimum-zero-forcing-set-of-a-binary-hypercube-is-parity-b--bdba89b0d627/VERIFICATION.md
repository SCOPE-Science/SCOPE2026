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

# Reproducibility and scope

Run from the directory containing these three files:

```sh
python3 verify_matrix.py
python3 verify_small.py
```

The exact finite outputs checked were `MATRIX_CERTIFICATE_PASS` and `ENUMERATION_CERTIFICATE_PASS`. The matrix checker verifies the square identity and exact matrix pattern for dimensions two through six and independently computes ranks modulo a large prime. The combinatorial checker exhaustively enumerates all subsets of the minimum cardinality in dimensions two through four and all smaller-cardinality candidates, then verifies ordinary forcing closure, parity counts and the absence of every token slide.

The infinite-dimensional statement is proved in `RESULT.md` by an algebraic family with a separate parity-supported kernel argument and a forcing injectivity lemma. Finite executions are corroboration only; they cannot verify the universal quantifier. No external inputs, internet access, or third-party packages are required. Python 3.8+ is sufficient.

The primary source date and MSC are independently visible at https://arxiv.org/abs/2009.00220. The total zero forcing number on binary cubes is known and credited. The new claim concerns all-dimensional parity balance and frozen optimal slides, not that previously known scalar count. No independent audit has been performed.
