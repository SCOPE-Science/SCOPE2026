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

Running `python3 verify.py` from the delivered file set checks every degree-zero-through-four Fourier frequency in ambient orders four, five, and six by direct enumeration of permutations. It separately implements the last-vertex signed subset recurrence and checks all eight connected or component-product canonical motifs. Exact integer arithmetic is used, with no floating-point tests.

Observed direct-enumeration nonzero counts by Fourier degree were `4: [1,0,12,0,3]`, `5: [1,0,30,0,140]`, and `6: [1,0,60,0,885]`. The separate subset recursion passed every motif assertion. These tests establish the finite seeds; graph decomposition and exhaustive shape classification in the proof establish all \(n\ge3\).

No independent audit or human mathematical validation has been performed. Published priority is assessed only under the stated bounded literature comparison.
