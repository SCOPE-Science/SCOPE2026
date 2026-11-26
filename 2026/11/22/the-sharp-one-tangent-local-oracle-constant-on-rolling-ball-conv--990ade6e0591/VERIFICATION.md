---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

If c=0 or the full ball minimizer is feasible, the output is exact. Otherwise write d0=-c/||c||, q=x+tau d0, and v=p-q. The support inequality gives n·d0>=0 when tau>0; if tau=0 and n·d0<0 the ray enters the rolling ball, a contradiction. The relaxed solution is in the tangent plane (the unconstrained solution is outside the halfspace or on its boundary). Since q is feasible for the relaxation, d0·v>=0 for every minimizer, including a tie. Hence s^2>=||p-x||^2=||v||^2+tau^2+2tau d0·v>=||v||^2. Projection into the tangent ball is feasible in K, does not increase distance to q, and moves by a nonpositive multiple of v+rho n, whose scalar product with q-x is nonnegative. Expanding the two distances to x proves locality. The excess objective is bounded by ||c|| times the exact displacement sqrt(rho^2+||v||^2)-rho, giving both displayed bounds. On the disk, at x=rho e1 and s=rho eps, the positive tangential component eps^3 forces the unique relaxed solution x+s e2; the disk support point rho d_eps lies in the local ball since its squared distance to x is at most 2rho^2 eps^6. The repaired support gap is rho(1-(sqrt(1-eps^6)+eps^4)/sqrt(1+eps^2))=rho eps^2/2+O(rho eps^4). Thus the uniform coefficient cannot be reduced. The supplied disk tests were inspected, not run; their tolerances and finite scope do not bear the proof.

## originality

PASS

Best-of-knowledge pass for the sharp coefficient, in particular the matching loss witness for the same deterministic construction with a unique relaxed solution. Hazan's Lemma 2.3 states 2/rho for exactly this oracle. Its proof already establishes the nonnegative cross term that implies ||p-q||<=s by expansion, so the stronger upper estimate is a short consequence of existing proof ingredients, not a new oracle or independently novel upper-bound mechanism. The verified prior sources do not give the matching lower gap relative to the true local optimum.

## value

PASS

The same oracle now has a quantified sharp performance limit, not merely a smaller valid coefficient. The disk construction shows that no analysis of this algorithm can uniformly improve its quadratic guarantee under the same assumptions, even if ties never occur. This separates an analysis improvement from an algorithmic limit and does not promise an improved convergence order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
