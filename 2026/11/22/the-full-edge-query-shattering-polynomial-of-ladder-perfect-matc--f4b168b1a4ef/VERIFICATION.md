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

# Verification

The included executable `full_checker.py` requires only Python 3 and is run with:

```bash
python3 full_checker.py
```

It constructs each ordinary two-row ladder from its physical vertices and edges, then recursively enumerates graph-theoretic perfect matchings without using the column-tiling recurrence. For every physical support at widths one through six, it directly tests all Boolean traces against the explicit theorem's three structural conditions. It subsequently checks every support in the rung-plus-one-horizontal-per-cut quotient universe at widths seven, eight and nine, and checks the integer coefficient sum against the recurrence through one hundred columns. It checks the top-layer formulas and exhibits the two facet cardinalities of the shattered-support complex at six columns. Total direct support comparisons: 246,930.

The separately executed source output is embedded in `full_checker_output.txt`; verify by rerunning instead of trusting the saved log. The mathematical proof is the all-parameter construction, alternating-run criterion and formal-series calculation in `RESULT.md`. The exhaustive finite evidence does not by itself certify the infinite theorem, historical originality, mathematical importance or any independent review.
