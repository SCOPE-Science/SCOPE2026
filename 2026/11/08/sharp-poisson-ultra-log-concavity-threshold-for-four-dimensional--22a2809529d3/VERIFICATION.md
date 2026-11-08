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

# Reproduction and limitations

The executable `verify.py` requires only Python 3 standard libraries. Run `python verify.py`. It calculates the five closed-form intrinsic volumes, checks normalization and the three exact derived ratio identities across 181 interior aperture samples, proves no universal statement by enumeration, brackets the one numerical root and checks both sides of its phase transition. The universal proof is analytic: the positive derivative of the scalar function \(R\), together with exact endpoint limits and elementary comparisons involving \(\pi^2\), handles every allowed aperture.

The observed numerical output is reproducible but its float tolerances are not interval-arithmetic error certificates. The decimal cutoff is presented as a rounded approximation, not an algebraic number. The exact cutoff is the unique root of \(R(\beta)=2\), and the proof of existence and uniqueness uses calculus only. No independent audit was performed.
