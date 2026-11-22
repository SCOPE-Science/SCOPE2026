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

The analytic result is based on a stationary clipped exponential-run renewal kernel. Its exact wall-force identity follows from a renewal reward calculation and Stieltjes integration. The uniform interior-mass estimate bounds the approximation by \(H(s)\int_0^s H(t)\,dt\); elementary Laplace asymptotics then prove the three response classes. `checker.py` ran successfully with NumPy and SciPy and reported 98 deterministic assertions; it compares exact integral kernels and finite-cell stationary solutions for dimensions one, two and three, including the closed-form one-dimensional result. This is self-review and does not constitute independent validation. Finite-grid tests do not establish the asymptotic results; the proof does.
