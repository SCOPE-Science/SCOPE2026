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

Run `python CHECK.py` with Python 3, NumPy, and SciPy. The checker (a) reconstructs cardinal B-splines from a separate numerical B-spline implementation, (b) tests the exact order-two Zak multiplier on a grid, (c) checks the compact Zak sum against the Poisson Fourier-alias series for six orders and multiple phases and positions, (d) tests partition of unity, and (e) compares numerically optimized representative lower symbols against the analytic constant. The checker completed with the message `CARDINAL_SPLINE_HIGH_ORDER_CHECKS_PASSED 789`.

These finite tests cannot establish the asymptotic limit; the analytic certificate is the unique nearest-alias reduction with uniformly exponentially bounded tails, the strictly convex sinc-power minimization on a fixed frequency interval, and the separated outer-frequency estimate, all detailed in `RESULT.md`. The exact frame-symbol normalization is checked at order two and obtained algebraically from the Walnut representation. The independent audit has not been performed.
