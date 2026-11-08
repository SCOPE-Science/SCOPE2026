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

Run `python3 verify_cherry_path.py` with a standard Python installation; no third-party package is needed. The program computes independent Catalan-root recurrences for the count, cherry sum, path-length sum, and mixed sum through 55 internal vertices. It compares every coefficient with exact central-binomial expressions and confirms the strict sign classification using exact rational arithmetic. It also recursively generates all ordered Catalan full binary tree shapes through 11 internal vertices (58,786 shapes at the largest order) and checks every individual tree's cherry and path-length statistics against the recurrence totals.

The verified output contains `EXACT_CHECKS_PASSED 82878`. The computed covariance examples include \(-4/25\) at \(n=3\), \(-20/49\) at \(n=4\), and \(-46/63\) at \(n=5\). All computations are finite; the proof for all \(n\) is the root generating-function argument and algebra in `RESULT.md`.

The work makes no assertion that the result has been independently audited or externally certified. Bibliographical completeness and behavior under other tree laws are not established.
