---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Lee-Guzmán et al Proposition 10.4 eq (51) supplies an exact direct-integral 2x2 Hermite Gram matrix for the strip. Integrating h0,h1 explicitly gives matrix entries A,B,C and at x=0 top eigenvalue erf(a), with positive curvature 4ae^-a²/sqrt(pi), so zero is strictly locally minimal. For a↓0 compact-uniform rank-one Gram convergence and a Gaussian trace tail yield maximizers |x|→1/sqrt2 and M(a)/a→4e^-1/2/sqrt(pi). For a→∞, Q=I-Γ is sum of two positive Gaussian-tail Gram matrices; determinant expansion, Mills ratio and the lower-bound localization inequality force ax-log(2a)=O(1). On this scale lambda_min(Q) is e^-a²/(2sqrt(pi)a³)(e^{2s}+e^{-2s})(1+o(1)) uniformly over bounded s, minimized at s=0, giving sharp leakage and optimizer displacement. Independent high-precision evaluation at a=3,5,8,12 showed the normalized competitor leakage tending toward one. Fiber maximizer is not asserted to be a global L2 eigenvector.

## originality

PASS

Primary Lee-Guzmán et al 2023 matrix-symbol theorem explicitly covers the exact direct-integral reduction (not new), but inspected Proposition 10.4 and surrounding sections do not state the off-center every-a curvature or sharp optimizing logarithmic displacement and inverse-cubic leakage. Prior first-Hermite STFT strip theorems have a one-channel projection convention and different optimization. Best-of-knowledge PASS for new asymptotic norm and location.

## value

PASS

The natural two-mode polyanalytic Fock localization norm is improved by a full factor a² in its Gaussian leakage when optimized over a drifting Hermite fiber. This supplies a sharp quantitatively useful shape/location asymptotic and proves noncentrality for all strip widths, rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
