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

The companion `verify_kneser.py` checks the full two-time-layer update matrix over the prime field for ground-set sizes 4 through 10, nine fixed-space dimensions per size, and each asserted global order. It additionally exhausts all 531441 configurations at size 4 using a separate vertex-neighbor implementation. The captured output is in `verification_output.txt`; the program uses Python's standard library alone.

The proof of the infinite-family claim is in `RESULT.md`, including the incidence factorization, the three Jordan cases, the temporal size-four lemma and the primitive-state count. Finite experiments alone do not prove any unrestricted statement. Extension fields are handled algebraically by scalar extension of the prime-field Jordan form; they were not individually exhaustively tested. Independent audit has not been performed.
