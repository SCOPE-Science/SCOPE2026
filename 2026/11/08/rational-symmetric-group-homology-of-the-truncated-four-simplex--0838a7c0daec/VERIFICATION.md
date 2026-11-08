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

The standalone `verify.py` implements the finite proof calculation in exact rational arithmetic using only Python's standard library. It enumerates each face from the partial-map definition, constructs each signed boundary column, and performs complete column elimination with `fractions.Fraction`. All image ranks and generator-action traces are computed from these actual exact bases. The program checks the chain actions of a transposition and a five-cycle on every positive-dimensional simplex, then verifies the seven class traces and the invariants over all 120 permutations.

Observed results: face vector `(20, 150, 520, 815, 444)`, augmented ranks `(1, 19, 131, 389, 421)`, reduced rational Betti ranks `(0, 0, 0, 5, 23)`, rational characters for degree three `(5, -3, 2, 1, -1, 0, 0)` and degree four `(23, 1, -1, -1, 1, 1, 3)` in the class order recorded in `RESULT.md`. The output ends with `TRUNCATED_FOUR_SIMPLEX_S5_MODULES_EXACT_PASS`.

The check is finite and specific to this graph. It does not compute integral Smith normal forms, prove the integral lattice structure of the homology, or certify publication priority. No independent external audit has been conducted.
