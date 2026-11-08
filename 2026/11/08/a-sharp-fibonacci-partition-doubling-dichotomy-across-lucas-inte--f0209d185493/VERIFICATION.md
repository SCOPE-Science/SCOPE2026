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
Run `python verify.py` (Python standard library plus optional `mpmath` used for an independent Bergman-expansion check). The primary count implementation is an exact recursive subset decomposition over distinct Fibonacci entries. The proof uses the exact integer boundary relation R(F_j+3)=j-3, published interior gap transfers, and Lucas interval parity. Executing the embedded checker returned `VERIFY_OK parameter_integers=218 equality=92 strict=126 endpoint_cases=4`. The finite numerical checks validate examples, not infinitude. The recorded scientific status is self-reviewed; no independent audit has been performed.
