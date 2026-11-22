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

# Verification notes

`verify_trigram_dp.py` computes every five-neighborhood deletion-change vector and exhausts the finite suffix/profile-class recurrence for all input lengths four through twenty. It returns the complete length-by-length maximum table and verifies the witness construction for twenty-five explicit lengths. `independent_brute.cpp` computes each deletion profile from scratch for all binary words of lengths one through nineteen and checks eleven explicit witnesses at lengths twenty through thirty. All checks were actually executed, and their text outputs are bundled as `dp_output.txt` and `brute_output.txt`. Recompile and rerun using the commands in `RESULT.md` to reproduce the finite certificates. The formula for infinitely many lengths is proved mathematically by the preserved local-context witnesses, not by any finite test.

The two programs have different logical foundations: the first explores equivalence classes of local edit contexts, whereas the second directly enumerates source words and recomputes output profiles. The latter is a limited-length independent computational cross-check, not an independent audit of the mathematical claim. Priority searches do not certify mathematical uniqueness; one plausible recent manuscript was available only through its abstracts.
