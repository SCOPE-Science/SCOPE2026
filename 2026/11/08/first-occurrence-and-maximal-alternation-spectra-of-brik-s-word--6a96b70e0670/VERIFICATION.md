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

Run `python3 check_alternation.py` with Python 3.8 or newer. The code constructs 19 exact finite iterates, verifies their lengths and boundary properties, finds the maximal alternating factor by an independent linear scan, and directly checks all alternating factors of lengths 1–8 against the claimed first positions. It checks the first 010101 occurrence in stage seven and the integer arithmetic for the next, symbolic witness. These tests passed at packaging.

The infinite statement is proved in `RESULT.md` by an induction on the first occurrence of alternating powers. The next stage is too large to generate explicitly; its existence follows from the already present finite source window and fixed suffix, rather than from a finite enumeration. Independently auditing this induction and historical priority is not part of this verification.
