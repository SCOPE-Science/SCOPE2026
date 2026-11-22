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

The exact equilibrium relation \(s=1+t/s\) and the \(2k\)-dimensional spatial Fourier characteristic polynomial are derived from the stated recurrence, not fitted from simulation. The derivation of the Schur–Cohn inequality and the sign, uniqueness, transversality, and parity arguments are given in RESULT.md. The cubic-in-frequency decomposition is not a truncation: it includes all \(k\) spatial modes.

Running `python CHECKER.py` in the standalone package returned a PASS line after checking fourteen ring sizes. The first critical gain for \(k=3\) was \(0.820357195636\) to displayed precision, and every tested ring was strictly contracting below and expanding above its respective exact threshold. Finite computations support the symbolic result but do not prove it for arbitrary ring size.

The endpoint \(t=t_k\) is expressly classified as a *spectral* crossing only. The existence or type of a nonlinear bifurcation, nonlinear critical stability, and publication priority have not been independently validated.
