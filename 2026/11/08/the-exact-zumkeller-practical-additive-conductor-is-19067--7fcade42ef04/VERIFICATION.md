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

The executable `checker.py` is the finite portion of the proof and requires no external dependencies. Execute `python3 checker.py` and compare its output with `verification_output.txt`.

The checker verifies that practical integers determined by ordered prime-power factors agree at all 358341 even candidates with the elementary ordered-divisor interval criterion. It checks every required residue class, all 208 small odd Zumkeller numbers by an exact divisor-subset test, the finite bridge, the special value 20177, and the obstruction 19067. Failure at any mandatory assertion aborts the certificate.

The unbounded tail requires the written proof that multiplying a Zumkeller number by a coprime integer preserves Zumkeller status, and the modular lifting argument from a bounded representative in each odd residue. The finite enumeration alone does not prove that unbounded assertion.

Independent audit: not performed. No formal proof assistant or third-party certification is asserted.
