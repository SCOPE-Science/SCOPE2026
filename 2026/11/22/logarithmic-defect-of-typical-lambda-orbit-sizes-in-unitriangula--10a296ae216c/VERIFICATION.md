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

# Verification of the finite-field orbit census

The attached `verify.py` uses the finite-field matrix multiplication formula directly to enumerate lambda orbits over prime fields in dimensions no larger than five. It compares the independently enumerated orbit-size multiplicities with the transfer result. It also verifies exact aggregate counts at five integer prime-power field orders for sizes through 21. The checker uses only standard Python modules. The prime-power \(q=4\) transfer test confirms polynomial integral normalization, not an independent finite-field orbit enumeration over a characteristic-two extension field.

The rigorous all-dimensional proof is in `RESULT.md`; a finite checker is supporting evidence only. The typical-size law uses an analytic geometric-holding-time argument. Neither historical uniqueness nor any external peer review is certified here.

Run with `python verify.py` and compare with `verification_output.txt`.
