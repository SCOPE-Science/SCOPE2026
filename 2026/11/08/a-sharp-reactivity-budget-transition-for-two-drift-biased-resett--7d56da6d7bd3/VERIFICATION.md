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

The drifted resolvent at r is G_r(y|x)=q^(-1)exp((mu(y-x)-q|y-x|)/(2D)); solving the two-sink rank-two system gives the exact B(k) with denominator 1+K/q+(1-c^2)k(K-k)/q^2>0. Renewal gives T=(1-B)/(rB). Local-time Laplace functional yields B(k)=-r integral exp(-rt) E[(L_+-L_-)^2 exp(-kL_+-(K-k)L_-)]dt<0, strict because paths hit only one site with positive probability. Endpoint derivative has sign (z-1)+[c(z+1)-2]K/q-(1-c)(1-cz)(K/q)^2 with negative derivative on K>=0, so one Kc. Symmetry comparison rules out upstream preference; endpoint and interior classification follows for each K, with c z<1 from q>mu. Numerically independently checked D=mu=a=r=1 threshold Kc~1.8149905664 and interior k/K~.74285 at 4Kc; finite-grid check supplements analytic proof.

## originality

PASS

Best-of-knowledge PASS: a published two-boundary Robin allocation theorem was read in full but assumes bounded interval, no drift and no reset, and proves interior optimum for all positive budget, unlike this sharp corner-to-interior full-line reset phase. The identified single-point resetting literature does not itself optimize two separate sink strengths. A more general two-point resolvent optimization theorem remains possible and is an explicit residual risk.

## value

PASS

Optimal reaction resource splitting between upstream and downstream partially absorbing targets is a natural design parameter; an exact unique bang-bang-to-split threshold is substantively different from fixed-reactivity diffusion or restart-rate optimizations, and strict concavity permits an exact global classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
