---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For p,q>3, the upper/lower first-integral matching gives a->a^(q/p) each half-flight, hence T_kappa(a)=a+2 sum_{j>=1}e^{-L kappa^j} for kappa=q/p>1, 0<a<1. With h=log kappa, half-line Euler–Maclaurin gives sum e^{-Le^{jh}}=E1(L)/h-a/2+(aL/12)h+O(h^3), proving exact constant cancellation and coefficient aL/6. Reindexing by floor(log_kappa 1/L) gives periodic P_kappa and O(L) remainder; differentiation of the absolutely convergent periodization and the Gamma Mellin integral gives nonzero Fourier coefficients. The critical return κ=1 and κ<1 dynamics follow directly from the power return. No finite test used to infer analyticity, no continuation asserted through the singular origin.

## originality

FAIL

A highly relevant earlier published same-family theorem gives the identical power-return map, complete global trichotomy, exact physical-time series, and the same nonconstant Gamma-Fourier log-periodic boundary correction for all positive integer monomial degrees. Real-exponent interpolation changes no mechanism; the coalescence correction is a direct standard Euler–Maclaurin evaluation of the published exact series. The principal newness asserted in the frozen package is already established.

## value

FAIL

The exact observable and nonconstant periodized logarithmic ripple are already known for the same sewed-focus model, including sharper absorption-time tails. The residual E1/h small-h expansion and aLh/6 correction result from routine Euler–Maclaurin applied to that known exact series; the real-exponent interpolation is an elementary change of parameters. There is no sufficiently new motivated invariant or boundary theorem surviving those strong implications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
