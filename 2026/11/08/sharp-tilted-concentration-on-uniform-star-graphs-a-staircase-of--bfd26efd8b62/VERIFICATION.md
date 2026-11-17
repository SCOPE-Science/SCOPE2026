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

For n>=3 and t>0, fixing hub=0 turns 1-Lipschitz potentials into the full cube [-1,1]^n. The Hessian of log centered MGF is t^2 times a strictly positive covariance form because the hub has positive tilted mass, so every maximum is a sign vertex. The consecutive ratio F_(k+1)/F_k strictly decreases; its threshold is exactly X_n(t) and yields ceil X_n(t), with adjacent ties only at integer X. The hyperbolic expansion proves X_n strictly decreases from (n-1)/2 to 0, giving floor(n/2)-1 switches. Direct limit gives p(t)=1/(2t)-1/(exp(2t)-1) and envelope (sinh(t)/t) exp(t coth(t)-1). Independently evaluated all k for n=3,4,5,11,27 at six positive tilts and checked the asserted maximizing k (finite corroboration, not an infinite proof). Source scripts/check_star_laplace.py was semantically inspected; exact-rational tests do not prove all n.

## originality

PASS

Best-of-knowledge new finite-star sharp centered exponential envelope and sign-count staircase, with path K1,2 explicitly excluded. Bobkov–Houdré–Tetali define graph sub-Gaussian/Laplace transforms and compute path and clique cases but not the >=3-leaf branching-star formula; Sammer–Tetali torus/cycle geometry is different. Search of published mathematical records found star-based heat or norm calculations, but not the centered star MGF switching law. No priority guarantee against unindexed general graph-concentration literature.

## value

PASS

This yields a complete and sharp extremizer and equality classification for a natural graph Lipschitz concentration observable, including finite-size tilt bifurcations and continuum-leaf asymptotics, beyond the routine variance expansion. A natural researcher studying star graph sub-Gaussian concentration needs the exact finite-n envelope and branch-dependent optimizer, even without a closed quadratic sub-Gaussian proxy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
