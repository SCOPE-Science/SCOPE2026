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

# Reproducible verification

The accompanying `check_book_facets.py` is a standalone Python 3 program using only the standard library; execute `python3 check_book_facets.py`. The program independently enumerates integer anchored graph-Lipschitz potentials for the two-hub triangular-book graph, applies the connected-tight-edge characterization as a combinatorial rank test, and computes squared Euclidean norms with `fractions.Fraction`. It checks the full norm-and-facet-size multiset against the formulas and verifies the exact tangent-normal ranks and second-shell degeneracies. The same program also checks algebraic inequality signs over a finite parameter range.

Observed execution:

`TRIANGULAR_BOOK_FACET_SHELL_CHECKS_PASSED facets=6138 norm_entries=6138 incenter_ranks=9 second_shells=9 integer_inequalities=499`

Direct exhaustive checks cover the book sizes \(1\le q\le10\) (including the excluded boundary \(q=1\)); inequality checks cover \(2\le q\le500\). Finite enumeration does **not** imply the all-integer theorem, uniqueness in the literature, or global optimization over continuous centers. Those conclusions are established by the analytic proof and its global antipodal-center argument in `RESULT.md`. This is self-reviewed work with no independent mathematical audit.
