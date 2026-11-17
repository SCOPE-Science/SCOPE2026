---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Under exact Lorits–Gubar Table 1 v(y)=4+3y,c(y)=12-2y, the clipped payoff h satisfies -1<=h<=49/68, so saturation reduces to sign-dependent positive part. Behavior x'=x(1-x)(v-cx)/2, opinion y'=(1-y)[h]_+ - y[-h]_+, resource n'=n(1-n)(3x-1). The behavior nullcline x=v/c meets h=0 once at Q=(1/2,1/2); on trapping strip 1/3<=x<=7/10 two boundary sinks P0=(1/3,0),P1=(7/10,1), and Q saddle with Jacobian [[-11/8,1/2],[0,15/32]]. Planar index eliminates cycles and saddle loops; Poincare–Bendixson gives global convergence in the strip. Convexity and h(x,1/2)=-11(2x-1)^2/16 force the one-sided y<=1/2 low-basin rule. Stable graph invariance with h<0 yields 44/103 quadratic curvature; logistic resource integrates exactly, giving path-dependent n_infty in low basin and n->1 elsewhere. Independent symbolic check confirmed Jacobian and curvature; finite trajectories alone are not global proof.

## originality

PASS

Best-of-knowledge novel complete global classification, exact one-sided half-opinion threshold, quadratic stable-manifold coefficient 44/103 and limiting environmental continuum for the precise published game. Original authors report illustrative bistability but not these rigorous all-initial-state claims; distinct game–environment dynamics in later analyses do not entail them.

## value

PASS

Transforms the source paper’s two sample trajectories into a complete rigorous all-initial-state dynamical trichotomy, a sharp, nonlinear one-sided decision threshold and a continuum of resource memory. Exact stable-curve curvature and clipped vector-field index analysis are substantive model-specific structural results, not just replotting bistability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
