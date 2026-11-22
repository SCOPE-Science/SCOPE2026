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

# Verification notes

The proof's nonstandard step is the two-variable corner area calculation. In variables \(r=a+b\), \(x=a/r\), the measure element is \(r\,dr\,dx\), the singular norm is \(2\sqrt{2(x^2-x+1)}/[r^2x(1-x)]\), and the integration region has exact homogeneous area \(T^{-1}\int_0^1\min\{T\delta^2/2,H(x)\}\,dx\). Each endpoint contributes \(\sqrt2\log T/T\), giving three corners times the uniform simplex density \(1/(2\pi^2)\). The contribution from noncorner boundary strips is only \(O_\delta(1/T)\).

Execute `python verify.py` with NumPy. The checker compares the closed weight formula to independent numerical solves, checks near-corner scaling, and approximates the transformed homogeneous integral at several large finite thresholds. It returned `CHECK_OK assertions=3024; finite diagnostics only`. Finite numerical tests do not establish the asymptotic theorem, which rests on the uniform Taylor estimate and exact area calculation in `RESULT.md`.
