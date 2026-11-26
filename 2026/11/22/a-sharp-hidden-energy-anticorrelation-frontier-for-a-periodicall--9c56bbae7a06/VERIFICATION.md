---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For J=diag(1,−1), KJ+JK=2aJ, so the unique stable periodic covariance is T₀K⁻¹+q(t)J where q′=−2aq+2δσ. Half-period antisymmetry fixes q(0)=−(δ/a)tanh(aτ). Integration of q(t)² on the positive half-period gives (δ/a)²[1−tanh(aτ)/(aτ)]; its mean over both halves is zero. The globally randomized phase gives time translation invariance. Conditional future increments have mean zero, so the covariance at lag h≥0 is e^(−Kh) times the averaged one-time covariance, and the opposite lag is its transpose. The covariance of the conditional variances is −E[q²], whereas the off-diagonal covariance is the constant −kT₀/(a²−k²); conditional Wick pairing thus adds exactly twice its square. The marginal fourth cumulants are 3E[q²], and the mixed one is −E[q²]. F increases strictly from 0 to 1 because the numerator of F′ has derivative 2z sech²(z)tanh(z). Thus for k≠0 a finite crossing requires R>√2u/(1−u²), and some R<1 meets this precisely when 0<u<√(2−√3). Equality in the contrast condition gives a zero only at infinite half-period; k=0 is strictly negative at every positive half-period. The illustrative parameters give target 128/729 as stated.

## originality

PASS

The scoped contribution is the exact fourth-order sign frontier in a phase-randomized thermal OU pair despite its whole equilibrium covariance function. Neither covariance camouflage by itself, Gaussian phase mixing by itself, nor sign changes in unrelated periodically driven observables are claimed new. The resolved related indexed papers use materially different models or observables.

## value

PASS

In a natural symmetric thermal model even the whole second-order stationary time series fails to distinguish the switched baths from equilibrium. Negative squared-coordinate covariance is impossible for a centered Gaussian pair, and this result says exactly when it is visible and when no permissible contrast yields a crossing. It supplies a diagnostic regime and a sharp limit on it, rather than merely the existence of non-Gaussian phase mixtures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
