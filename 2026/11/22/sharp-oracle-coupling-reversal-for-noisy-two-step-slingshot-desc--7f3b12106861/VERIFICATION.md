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

# Verification of the coupled Gaussian slingshot result

The finite-horizon and stationary laws follow analytically from the paired recursion, independent-pair geometric series and an attainable Cauchy–Schwarz inequality on two orthogonal eigenmodes. Strict equality yields the unique optimal coupling for all parameters on either side of the isolated tie at \(r=1\). Stationary second moments require strict two-step contraction, namely \(0<r<\sqrt2\).

`verify.py` uses only Python's standard-library `fractions.Fraction`. From its containing directory run `python verify.py`. It tests the paired polynomial identity, isotropic noise covariances under exact rational orthogonal couplings, optimality comparisons across 129 admissible rational-step pairs, and finite horizons of one, two and seven pairs. Expected output: `PASS: 5676 exact orthogonal/finite-time comparisons, analytic formulas and five rational witnesses`. Exact witness risks at unit slope and unit marginal variance are: at \(r=3/5\), identical-noise risk \(18/41\) and independent-noise risk \(118/41\); at \(r=6/5\), coordinate-swap risk \(26/7\), identical-noise risk \(36/7\), and independent-noise risk \(86/7\).

These finite tests do not prove the continuum or establish novelty; the proof uses exact operator algebra and Gaussian-marginal equality cases. The coupled second oracle need not remain unbiased conditional on the random intermediate iterate. No performance guarantee for standard independent stochastic-oracle access or nonlinear games is asserted. This package does not constitute independent mathematical validation.
