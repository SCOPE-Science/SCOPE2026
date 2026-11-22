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

# Verification record

The theorem is verified analytically by a strict-negativity formula for the third derivative of \(f_a\), a midpoint inequality for its first derivative, a uniform negative upper-mean endpoint, and an exact square-difference identity at the lower-mean endpoint. The quadratic \(G_a(d)=7d^2+(9a-3)d+a(3a-2)\) has either no feasible positive root or exactly one; the radical root and the feasible boundary value \(G_a((1-a)/2)=(a+1)^2/4\) establish the complete classification. All equality cases are explicitly identified in RESULT.md.

The self-contained Python program CHECK.py was run from its delivered source path using only the Python standard library, with 33,560 passing diagnostic assertions. Its exact-rational algebra checks and finite floating-point samples validate the implementation of illustrative identities and examples, but do not constitute an exhaustive or machine-formal proof for all real parameters. Independent validation has not been performed. Original development-rate modelling is empirical, and the derived rate-summation classification has no field calibration attached.
