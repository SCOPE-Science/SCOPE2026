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

The theorem is established deductively by the six proof steps in `RESULT.md`. Independently check the finite calculations with `python3 verify.py` from a directory containing the two files. The checker enumerates 21,096 full-rank binary two-row generator-column sequences of lengths 2–7 and all 19,902 ordered realizable-profile pairs for lengths 2–12. For each profile pair, it directly minimizes exact rational distortion over six matchings, then separately compares the sorted-ratio formula, global maximum and complete equality classification. Expected terminal line: `CHECK_OK` (printed before detailed counts).

Finite computation does not establish the theorem for larger block lengths; that scope is supported by the uncrossing and equality arguments. The correctness and novelty review here is same-model only. Independent mathematical audit and exhaustive historical priority verification have not been performed.
