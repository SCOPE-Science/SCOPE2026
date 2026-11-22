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

Run `python3 verify.py` with Python 3, standard library only. The source reconstructs Dung's admissible/preferred/stable semantics by finite set enumeration on 340 labelled simple forests with at most five vertices and all 9987 self-loop markings; no semantic result is assumed inside this independent finite checker. It separately compares all path markings of orders 0 through 14 with a 16-state exact transfer construction. It verifies the full 16-state characteristic polynomial and the unique primitive cyclic component, as well as the algebraic identity `(T**5 - T**4 - T**3 + T - I)*B == 0` over the integers (implemented as sparse matrix-vector multiplication), and the induced recurrence through order 44. Actual output: `VERIFY_OK forests=340 loop_markings=9987 path_orders=0..14 transfer_order=44 exact_PTB=zero`.

The finite enumeration is not presented as a proof for arbitrary forests; the complete structural proof is in RESULT.md. The exact matrix identity, coupled with the explicitly defined transfer and initial values, implies the generating function for every path length. Dominant-root decimal values are approximations of the exact algebraic definitions, not separate certified decimal certificates. No independent external review or validation was performed.
