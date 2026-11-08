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

# Reproduction and limits

Run `python3 verify_certificate.py` and `python3 verify_direct.py` with Python 3 and no external dependencies.

The first script derives the Rule 110 de Bruijn matrices, checks the two-state zero-gap matrices and their exact Perrin recurrence, verifies the 19 integer-matrix base inequalities, checks the exceptional ordered pair, and compares the zero-gap trace with the full de Bruijn trace on all indexed outputs through length eleven. Its all-length inference uses the explicitly proved bivariate recurrences for the difference matrices and the merger argument in `RESULT.md`.

The second program computes each cellular-automaton update directly for every one of the \(2^n\) binary inputs on each cyclic ring of size \(1\le n\le18\), yielding complete observed inverse-degree maxima and maximizing outputs. This is a finite independent sanity test, not an infinite proof. Both scripts report `CERTIFICATE_OK` and `DIRECT_OK` upon success. No external scientific audit or independent validation has been performed.
