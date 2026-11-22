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

The proof uses exact forward moment identities for the stated three-state model, an exact rational-coefficient first-order equation for the Laplace transform, the positive integrating factor, and the monotone Laplace Tauberian theorem. The latter is the mathematical basis for the infinite-time statement.

The accompanying `verify.py` was executed with `sympy` and `scipy`: exact symbolic residue calculations passed for both coefficients, the physical critical relation held identically, and independent ODE checks passed for rate sets \((\lambda,\eta,v)=(1,3,1)\) and \((2,5,2)\), with both subcritical and critical reinforcement. The normalized critical moment increased from approximately \(0.85\) to \(0.94\) times its limiting leading form over sampled times, as expected for a slowly converging logarithmic asymptotic. These finite samples alone do not prove the limit.

No independent audit or external certification has been performed. The underlying model, transform equation, and phase boundary are established prior results; the specific logarithmic equality law and subcritical coefficient are the assessed addition. A separate publication-priority comparison may identify broader implicit coverage.
