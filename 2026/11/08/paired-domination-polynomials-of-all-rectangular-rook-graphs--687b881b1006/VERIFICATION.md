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

# Reproducible checks and limits

The theorem has a complete symbolic proof in `RESULT.md`: domination iff no simultaneously empty row and column; matching iff each nontrivial incidence component has even edge cardinality, proved using even-indegree orientation; the labelled exponential formula with a signed-edge filter; and row/column fiber counting for minima. All checks below were performed on self-contained Python scripts in this package using the standard library.

Run `python verify_direct.py` to enumerate vertex subsets of seven small rook graphs. It tests domination square by square and tests perfect matching in the induced selected graph via recursive mask matching. It does **not** use the component-parity theorem. For each board it checks every coefficient against a reference table and prints a final `DIRECT_PASS` line. See `verify_direct.out` for the full recorded output.

Run `python verify_series.py` to reconstruct the exact \(P_{m,n}\) coefficients via labelled binomial polynomial multiplication and the formal identity \(E^2=F(z)F(-z)\). The coefficients of \(E\) are derived recursively in total vertex-number order, and the row/column isolation terms are handled by finite alternating sums. Its seven small-board polynomials match direct enumeration coefficient for coefficient, and it computes leading coefficients for \((5,5)\) and \((5,6)\). A final `SERIES_PASS` line is recorded in `verify_series.out`.

Run `python verify_minima.py` to count row-to-column occupancy assignments independently, with even column-fiber counts and the doubled-row two-special-column parity condition. It validates the ten board minima listed in `verify_minima.out` and prints `MINIMA_PASS`.

All three scripts were executed successfully. The finite tests cover exactly the dimensions explicitly listed; they are not proof for all larger dimensions. The symbolic proof supplies those unbounded quantifiers. Neither historical priority nor independent scholarly validation follows from program execution. No external certification has been performed.
