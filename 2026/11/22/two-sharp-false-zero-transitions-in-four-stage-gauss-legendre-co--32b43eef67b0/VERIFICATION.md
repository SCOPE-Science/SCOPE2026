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

# Verification of the reported scalar-collocation result

Run `python verify.py` with SymPy installed. The verifier uses only exact integers, rational arithmetic and algebraic-number signs for its scientific assertions. It checks the residual defining the four Gauss collocation conditions, the positive endpoint sum-of-squares identity, the full discriminant polynomial, the two isolating intervals via complete Sturm variations, the exact four-stage root counts at three rational parameter values, the absence of triple roots at the transitions, and the signs of every Gauss-node value at those test parameters. It separately prints floating-point approximations of the two algebraic transition parameters and their zero locations for human orientation; these approximations do not constitute the proof.

The proof relies on continuous polynomial roots, the nonvanishing endpoint and the uniqueness of the two positive discriminant roots. Finite checks alone would not certify the continuous sign diagram; the analytic argument is included in `RESULT.md`.

This is a scientific reproduction record only. No independent audit or external mathematical validation has been performed.
