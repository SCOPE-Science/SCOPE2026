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

# Finite corroboration and proof boundaries
The accompanying standard-library `checker.py` independently implements the exterior multiplication table by bit-mask inversion signs. It enumerates all \(3^{10}\) linear-plus-quadratic inputs over \(\mathbb F_3\) and checks the fiber size for **each** of the \(3^5\) possible radical square targets. Over \(\mathbb F_2\) it enumerates all \(2^{10}\) corresponding inputs and confirms the square is always zero. It constructs and checks two explicit square roots for 64 deterministic pseudorandom prescribed targets with nonzero square scalar part each over \(\mathbb F_3\) and \(\mathbb F_5\).

The checker output is preserved verbatim as `checker_output.txt`. The tests do not establish the theorem for infinitely many finite fields; the exterior-algebra rank and support-plane proof in `RESULT.md` does. The proof relies on standard nondegenerate alternating-form counts and on the rank-two Plücker description, both explicitly explained there. The zero-square total is already implicit in prior Jordan-stratum results, whereas the fixed nonzero target counts are independently proved here.
