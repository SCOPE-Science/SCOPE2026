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

The mathematical argument is self-contained in `RESULT.md`. The following two checkers use only Python standard-library functions and were executed from the supplied paths:

- `python3 verification/verify_capacity.py`: exhaustive mixed-radix construction and symbolic recurrence through budget 24, including 1,000 inverse threshold checks; actual output in `verification/verify_capacity.out`.
- `python3 verification/verify_graphs.py`: every topologically ordered directed multigraph with two to five vertices and one to nine edges; actual output in `verification/verify_graphs.out`.

Finite enumerations do not prove the theorem for arbitrary budgets or graph orders. That follows from the inductive path bound, strict increase, and equality analysis in `RESULT.md`. The evidence does not constitute independent review or proof certification.
