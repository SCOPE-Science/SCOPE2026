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

# Verification and limitations

Run `python3 verify.py` in the same directory as this file. Its exact-integer tests directly evaluate four-point and five-point polynomial congruences, classify every tested local midpoint and step by truncated valuations, count the local/global solutions, check multiplicativity for 49 moduli between 5 and 150 coprime to 6 (375049 index/step pairs), and exhaustively test the additional prime-power moduli 125, 625, 343, 121, 169, and 289. The script further tests 10000 deterministic random pairs at 3125 and explicit five-adic nonextension examples.

Expected output begins with `VERIFY_OK` and describes the counts. There are no external libraries or runtime-generated source files. The proof itself is the symbolic second-difference identity, exhaustive valuation argument, local counting, and the Chinese remainder theorem in `RESULT.md`; the finite tests cannot by themselves establish the statement for all moduli.
