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

The complete enumerator `verify_direct.py` evaluates all \(3^{n+1}\) labelled colorings for each rim length \(3\le n\le11\) using the full neighbor-multiplicity update. It returned fixed-state counts, ordered by rim length, of \(3,15,3,21,3,39,3,93,3\), matching the theorem.

The separate transfer checker `verify_transfer.py` compares balanced cyclic-word coefficients with the run-composition formula for all even rim lengths from four through eighty. All assertions passed, including the large exact count \(B_{80}=4322201369563482\).

Both checkers use Python's standard library, run as `python3 verify_direct.py` and `python3 verify_transfer.py`, and need no external data. They establish finite test agreement only. The full all-length assertion follows from the local rim/hub argument and marked-run double count; the asymptotic claim additionally uses the positive-variance, aperiodic finite-state transfer local central limit theorem proved in `RESULT.md`. The analytic derivation has been reviewed only at the same-model level; no independent validation was performed.
