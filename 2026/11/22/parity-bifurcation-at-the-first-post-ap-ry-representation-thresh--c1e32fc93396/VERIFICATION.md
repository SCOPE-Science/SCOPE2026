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

The accompanying `verify.py` implements an exact unbounded-integer three-coin dynamic program and checks all predicted low-multiplicity gap components for integers \(3\le a\le160\) beyond the final gap. It additionally cross-checks coefficient vectors by direct enumeration for \(3\le a\le21\). The proof, not finite testing, establishes unrestricted validity. No external independent validation has been performed.
