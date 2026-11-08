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

The reported computation uses only Python 3 standard-library functionality:

`python3 verification/check.py`

Observed output:

`BOOK_ORIENTATION_ONLINE_PASS b=0..6 conditional_states=84 recurrence_triples=64000`

The program independently tests all orientations against graph-cycle detection for books of zero through six pages, recomputes binary mistake-tree ranks for those sizes, checks 84 nonisomorphic conditional parameter triples by direct recursion, and verifies the closed-form recurrence on 64,000 parameter triples. It also checks that every shattered support of books through four pages is exactly an edge forest.

Finite enumeration is supporting evidence only. The all-parameter conclusion follows from the structural residual-class recurrence and induction in RESULT.md. No external proof assistant or independent mathematical review was used.
