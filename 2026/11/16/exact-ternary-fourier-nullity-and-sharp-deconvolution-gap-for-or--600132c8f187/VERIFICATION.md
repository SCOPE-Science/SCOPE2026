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

`python3 verify_ternary_row.py` enumerates the \(42\) order-four alternating-sign matrices by necessary-and-sufficient row/column partial-sum constraints, tests all \(3^9\) reduced frequencies in exact integer phase counts, and exhaustively tests every one- and two-coordinate ambient frequency.

`python3 verify_ternary_triangle.py` uses the independent monotone-triangle bijection and an exact nine-dimensional Fourier transform in \(\mathbb Z[\omega]\). It reproduces all \(53\) squared-magnitude levels and Parseval's identity without floating-point comparisons.

Cross-comparison of the two implementations confirms the same \(42\) signed matrices and identical full reduced squared-magnitude multiplicities. The complete distribution is in `SPECTRUM.json`, and all computations are confined to order four. No claim about larger sizes or independent external validation is made.
