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

The finite-section proof uses the exact continuant \(d_{3r}=(-2)^r\), \(d_{3r+1}=2(-2)^r\), \(d_{3r+2}=0\), a uniform inverse-decay bound for the interior block, and a two-channel Schur complement. The independent spectral gap argument is the uniform Schur bound, not a finite eigenvalue sample. The code `checker.py` checks exact finite identities and high-precision signs for small levels. Numerical bisection does not certify all sizes or establish priority.

Self-review was completed; no independent review, external validation, or formal proof assistant verification has occurred.
