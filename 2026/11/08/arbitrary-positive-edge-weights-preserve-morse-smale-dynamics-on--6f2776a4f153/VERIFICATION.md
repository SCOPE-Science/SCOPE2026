---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The quotient map is z+hKA sin(z), K=[[2,-1],[-1,2]], A=diag(a,b). Its maximal weighted-Laplacian eigenvalue is Λ=a+b+sqrt(a²-ab+b²); Hessian bounds imply strict descent for V=a cosx+b cosy, and I+hKA diag(cosx,cosy) is positive definite in a symmetric conjugation for h<1/Λ. Degree-one local diffeomorphism on the torus is globally invertible. All recurrence is confined to four hyperbolic fixed points. The triangle 0<=x,y<=π, x+y>=π is forward invariant because siny<=π-y<=x and sinx<=π-x<=y, and 2ha,2hb<1. At p=(0,π), unstable slope r=(a+b-sqrt(a²+ab+b²))/b is in (0,1), stable slope R>1; at q=(π,0) the slopes swap sectors. Thus both unstable branches enter this triangle or its centrally reflected image; neither triangle can meet a saddle stable manifold near an endpoint. All saddle unstable branches reach the unique sink; source/sink stable-unstable intersections are automatic transverse. At h>=1/Λ the multiplier 1+hΛ cos t vanishes on diagonal x=y=t for suitable t, proving nonlocal invertibility. Independent bounded tests confirmed triangle invariance, V descent and slopes for six highly unequal weight pairs; those samples do not prove absence of connections.

## originality

PASS

The October 7 2026 Buescu–D’Aniello–Oliveira paper establishes a potential, global convergence and almost-global sink for positive weighted graphs but its advertised weighted Morse–Smale criterion has diagonal-dominance/conavity hypotheses on three-clock paths; it does not claim all positive edge ratios. The submitted invariant triangle provides an all-ratio transversality proof. The original source full text was not accessible in this run: arXiv OA/PDF attempts failed and authorized Oxford returned vpn_disconnected, so the claim that its theorem hypothesis does not cover extreme ratios is supported by abstract plus source-facing theorem references, not a freshly complete original paper inspection. This access limitation alone does not fail best-of-knowledge originality; a hidden stronger theorem is an explicit residual risk.

## value

PASS

In planar gradient-like maps, descent and a full-measure sink do not imply transverse invariant-manifold intersections. Removing weighted diagonal dominance in the smallest nontrivial open path is a meaningful structural extension and supplies an exact entire quadrant of parameter weights together with a sharp invertibility step. The invariant-triangle barrier is a substantive nonstandard dynamical lemma, not a routine stability-eigenvalue calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
