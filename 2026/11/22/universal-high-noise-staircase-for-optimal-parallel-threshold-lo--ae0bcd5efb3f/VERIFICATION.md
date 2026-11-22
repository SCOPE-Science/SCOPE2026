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

## Reproducibility
Run `python3 verify.py` from the directory containing this document. The program uses only Python's standard-library exact rational arithmetic. It enumerates every response sign vector and integrates conditional cell likelihoods explicitly for up to five queries; it checks the predicted weak-contrast staircase and directional perturbations. The recorded execution output appears in `CHECKS.txt`.

## What was checked
The actual packaged `verify.py` passed 40 exact-rational inequalities, including repeated-midpoint comparisons for the predicted offsets, outcome-label permutation invariance, weak-contrast gain scaling, and strict loss when a predicted location is moved by a small multiple of the squared signal contrast in the tested cases. The finite tests use contrasts \(1/8\), \(1/16\), and \(1/32\). The proof in `RESULT.md` separately establishes the arbitrary fixed query-count asymptotic via Walsh moment identities, a uniform remainder estimate, and an exact square completion.

## Boundaries of verification
No external formal proof certificate or independent audit is claimed. Finite arithmetic tests do not enumerate all real thresholds, all budgets, or all noise strengths. The theorem proves leading asymptotics only when the number of queries is fixed and bit contrast tends to zero; exact global optimizing locations at finite contrast are not supplied. Historical-publication priority remains qualified by imperfect literature coverage.
