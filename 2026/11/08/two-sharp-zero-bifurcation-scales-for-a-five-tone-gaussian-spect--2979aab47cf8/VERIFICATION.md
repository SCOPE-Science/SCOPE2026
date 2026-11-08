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

Execute `python3 CHECK.py` next to this file, using Python 3.8+ and no external dependencies. The checker separately computes direct midpoint quadrature of the original Gaussian STFT integral and the closed formula, verifies the integer discriminant factorization and exact rational boundary minimum, evaluates the roots in all three generic regions, checks both repeated-root cases with nonzero second derivatives, and verifies the reciprocal quartic at constructed zeros.

The executable tests sample representative real parameters; they do not establish a statement about all real parameters. The universal proof is the finite-degree exact algebra and elementary sign/continuity reasoning in RESULT.md. The special full text most closely related to spectral interference was inaccessible, and the claim has not received independent mathematical or literature-priority review.
