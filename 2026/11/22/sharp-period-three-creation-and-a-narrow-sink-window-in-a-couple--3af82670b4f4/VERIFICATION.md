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

The standalone checker `verify.py` verifies exact resultant factorization, linear subresultant, the trace/determinant identities on the nonfixed period-three polynomial, and the threshold cubic factorization. It also computes finite sample points for diagnostic purposes. These checks use the exact source files shipped in this package. Results apply only to the full real plane at self-coupling one with positive second coupling; they are not independent mathematical certification.
