# Fresh audit — SCOPE-20260907-009

Date (UTC): 2026-09-30

## Final claim

In the defined 8-state quarter-probability birth–death stratum, the endpoint hitting-time maximum is 6544, uniquely attained modulo the terminal row by the all-left-drift interior pattern.

## Correctness

**PASS** — The birth–death first-step recursion was reconstructed directly. A fresh exact Fraction enumeration of all 186,624 row-0-through-row-6 patterns reproduced maximum 6544, one maximizing pattern, exactly 10,046 distinct values, and the stated top five values. The coordinatewise monotonicity argument also proves the maximizing pattern without relying on the census.

Residual risk: The separately reported mixing-time bracket remains empirical/numerical and is not treated as part of the accepted exact theorem.

## Originality

**PASS** — Semantic published-results and web searches found the exact denominator-4, 8-state table only in this record. Standard birth–death hitting formulas cover the method, not this exact finite table, and no exact database/table for this slice was located.

Residual risk: This is a best-available literature search, not a proof that no private or obscure table exists.

The originality comparison explicitly checked equivalent formulations, broader coverage, exact databases/tables, and whether prior results imply the present claim.

## Value

**FAIL** — The extremizer follows immediately from coordinatewise maximization of the standard birth–death recursion once the finite grid is chosen. The particular combination of eight states and quarter-grid probabilities is not given an external mathematical motivation strong enough to distinguish it from an arbitrary denominator-restricted exercise, and the exact value 6544 has no demonstrated downstream need. The record itself characterizes the extremizer as unsurprising and the table as a compiled benchmark.

Residual risk: A concrete external application that specifically requires this denominator-4, eight-state benchmark could change the value assessment, but none was established in the package or literature search.

## Sources inspected

- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/009/RESULT.md — Full result inspected, including the exact recurrence, census theorem, and limitations.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/009/artifacts/exact_census.py — Actual exact Fraction census source inspected.
- https://github.com/SCOPE-Science/SCOPE2026/blob/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/07/009/artifacts/verify_exact.py — Actual independent Gaussian-elimination cross-check source inspected.
- https://github.com/Resultary/2026/tree/main/2026/9/7/SCOPE009 — Exact semantic search; own record was the only direct exact match.
- https://pages.uoregon.edu/dlevin/MARKOV/ — Standard birth–death/mixing reference searched as background; no exact quarter-grid 8-state table located.

## Overall disposition

FAIL
