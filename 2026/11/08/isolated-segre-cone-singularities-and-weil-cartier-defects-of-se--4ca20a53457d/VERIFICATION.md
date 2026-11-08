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

The geometric proof is the principal evidence for the full range \(n\ge4\). In `verify.py`, exact rational row reduction checks toric Cartier constraints for \(n=4,5,6,7,8\), the primitive-ray spanning check, the Cartier hyperplane representative, and the anticanonical threshold. Direct finite-field enumeration checks the defining rank-one conditions for \(q=2,3\) and \(m=2,3,4\); it does not by itself certify infinitely many dimensions. The local Segre-cone class-group computation uses the standard quotient of the Picard group of the Segre base by its hyperplane class. The preprint arXiv:2606.16482 was not available in complete text, so historical priority remains provisional.
