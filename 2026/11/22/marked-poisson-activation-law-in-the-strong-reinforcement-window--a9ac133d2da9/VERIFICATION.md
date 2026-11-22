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

# Reproducibility and verified scope

Invoke `python3 checker.py` in the same directory. This script is self-contained and uses only Python's standard library. It enumerates exact activation-indicator histories and the complete labelled activation-history process, checks both finite-dimensional distributions against the independent marked reference, and verifies the finite total-variation inequality using exact rational arithmetic. The captured output in `checker_output.txt` corresponds to a fresh execution of that exact file.

The analytic proof, not the numerical or finite checks, establishes the all-size coupling and the infinite Poisson process limit. The model takes a constant parameter \(a\) within each finite tree and permits \(a_n\) to vary across tree orders in the triangular-array theorem. No full-tree topology law, cover-time limit, or independence certification is claimed.
