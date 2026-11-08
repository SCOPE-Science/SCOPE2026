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

The proof uses a modular nilpotent tensor-sum decomposition and exact temporal primary modules. The following replayable, standard-library-only checks supplement that proof:

- `python3 proof/verify_matrix.py`: exact modular ranks and temporal fixed-space dimensions for \((m,d)=(3,1),(3,2),(3,3),(3,4),(6,1),(6,2),(9,1)\), including independently checked sharp matrix orders.
- `python3 proof/verify_states.py`: exhaustive state-by-state evolution of \(729\) states on \(H(1,3)\), plus deterministic state-level samples on \(H(2,3)\), \(H(3,3)\), and \(H(1,6)\).
- `python3 proof/verify_tensor.py`: exact integer recurrence checks for ten alphabet sizes and forty dimensions per size.

The captured expected output is in `proof/verify_matrix.out`, `proof/verify_states.out`, and `proof/verify_tensor.out`. Computations do not establish arbitrary-dimension correctness, nor do sampled states imply an exhaustive census; those assertions rely on the proof in `RESULT.md`. The historical literature comparison has limitations documented in `REVIEW.md`; independent audit has not been performed.
