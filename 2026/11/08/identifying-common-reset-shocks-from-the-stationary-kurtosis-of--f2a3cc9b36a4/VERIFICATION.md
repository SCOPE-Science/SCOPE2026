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

## Analytical checks
The stationary generator applied to five monomials gives a triangular, explicitly solved moment system. A separate Poisson-survival integral, conditioning on the absence of position resets while retaining independent internal resets, reproduces the same fourth moment, including the zero-exclusive-reset boundary. The linear generator identities for \(x\) and \(\omega\) give the complete stationary two-time covariance matrix and zero cross-covariances; strict positive differentiation proves the complete attainable interval and inversion.

## Reproducible checks
Run `python checker.py` with SymPy and mpmath. It checks algebraic identities symbolically, evaluates 72 independent integral parameter cases to high precision, and performs exact rational feasibility/inversion checks over a finite grid (680 integral and rational assertions overall). The independent derivations and the proof apply to all stipulated real parameters; these checks supplement rather than replace that proof.

## Scope of verification
The proof assumes independent Brownian noises, three independent homogeneous Poisson clocks with nonnegative intensities and strictly positive total reset rates, and the unique stationary law. No simulation-based infinity claim, finite-sample detection guarantee, independent audit, or external proof certification is asserted.
