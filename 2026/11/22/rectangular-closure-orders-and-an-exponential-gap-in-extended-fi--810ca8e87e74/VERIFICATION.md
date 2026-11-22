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

# Reproducibility

Run `python3 CHECK.py` with `CHECK.py` and `LINE_WITNESSES.csv` in the same directory; no nonstandard Python packages are required. The script exhaustively enumerates north/east paths and closure-admissible orders for the rank-reversing antichain on up to eight points, compares another 45 generic permutation point sets, and samples every positive-slope affine arrangement chamber exactly by rational arithmetic for two through thirteen grades. It checks the known 30-versus-32 six-grade discrepancy and the thirteen-grade polynomial bound.

The 30 rows of `LINE_WITNESSES.csv` give rational line parameters for each observed six-grade strict line order. The arbitrary-size rectangular closure theorem, count and line upper bound are proved in `RESULT.md`, not inferred from finite data. The six-grade nonrealizability contradiction is analytic. Numerical barcode endpoints are not compared: only degree-labelled combinatorial equivalence is claimed.

No independent mathematical audit has been performed.
