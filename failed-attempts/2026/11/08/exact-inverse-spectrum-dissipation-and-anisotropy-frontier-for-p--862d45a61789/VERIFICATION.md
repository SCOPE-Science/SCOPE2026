---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In real orthogonal Schur coordinates the drift is A=[[-a-b,h],[0,-a+b]]. The stationary Lyapunov equation forces D=B/2=-(A+A^T)/2 and tr B=4a. The diffusion eigenvalues are a±c with c=sqrt(b^2+h^2/4); strict positivity requires c<a. Every b<=c<a occurs, with spectrum unchanged, and stability and the Lyapunov equation give the same N(0,I). The current matrix W=A+D is skew with magnitude |h|/2, hence Phi=tr(W^T D^(-1) W)=2a(c^2-b^2)/(a^2-c^2). Substitution of c=a(K-1)/(K+1) proves the claimed curve. Phi'=(a^2-b^2)(1-K^(-2))/(2a)>0 on the feasible domain, so a feasible finite cap is attained at its upper endpoint. From C(tau)=exp(A^T tau), the off-diagonal lag difference has magnitude |h|e^(-a tau)sinh(b tau)/b, giving the stated Frobenius norm and its limiting bound. The boundary c=a is not in the model class. For tau>0 the lag supremum is approached and not attained; tau=0 is identically zero. The saturation is not non-identifiability from exact positive-lag norm data at fixed a,b, since that norm is strictly increasing in c.

## originality

FAIL

Troude–Sornette's earlier planar canonical drift and EPR/lag formulas already imply the complete frontier by stationary covariance matching and elimination, not just one example or a generic EPR identity. Every orientation of the frozen drift is orthogonally equivalent to their Eq. (3), and the required noise lies in their Eq. (9). Their Eq. (12) gives the exact rate, and the explicit propagator in §VI.2 gives the same finite-lag law. Eliminating the single drift parameter and observing monotonicity is mechanical. This is a claim-level implication, not an assertion that the prior paper expressly labels the eliminated quantity an anisotropy frontier.

## value

FAIL

The model question is motivated and the curve is usable, but the precise frozen statement is a routine covariance match, orthogonal coordinate choice and reparameterization of a previously solved planar model. Neither a finite cap nor the limiting bounded lag adds an independent invariant beyond those formulas. The record proves no separate statistical limitation from noisy lag observations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
