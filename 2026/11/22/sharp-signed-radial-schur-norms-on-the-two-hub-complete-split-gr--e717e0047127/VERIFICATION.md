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

An independent sharp bound avoids the frozen minimax step. Write a=(1+t)/2, b=1/n, u=|t|, q=a+b+2u. Hub-antisymmetric and leaf-contrast eigenvalues of M are nonnegative; the remaining block is congruent to [[a,t],[t,b]]. Thus M is positive exactly when kappa=t^2-ab<=0, giving the two stated roots and norm one in that region. Otherwise set d=kappa/q and V=d vv*, where v has entry 1 at each hub and -sgn(t) at each leaf. The corresponding block of M+V is congruent to [[a+d,t-sgn(t)d],[t-sgn(t)d,b+d]], with determinant zero and nonnegative diagonal. Elementary contrast eigenvalues are unchanged. Thus M=(M+V)-V is a difference of positive kernels. Combining their Gram factors with a sign on the second summand bounds the ordinary and all amplified norms by the common sum of their diagonals, 1+2d. For p proportional within the two classes as stated, let s be its hub mass. On the compressed constant plane, D_p V D_p has range spanned by (sqrt(s),-sgn(t)sqrt(1-s)); the range of D_p(M+V)D_p there is spanned by ((a+u)sqrt(s),sgn(t)(b+u)sqrt(1-s)). These are orthogonal at s=(b+u)/q. D_p V D_p then has its sole nonzero eigenvalue d on the negative line of D_p M D_p, which has trace one. The spectral-sign input gives the lower bound 1+2d, including degenerate contrast eigenvalues. Positivity and norm endpoints simplify as stated. For the infinite case, b tends to zero; finite compressions give the lower bound. Taking d=t^2/(a+2u) for t nonzero yields the same positive-kernel construction on every finite corner (remaining determinant b(a+d)>=0), with bounded Gram vectors, hence a normal completely bounded multiplier. At t=0 the multiplier is the diagonal expectation. This proves all operator, cb and limiting claims in the specified parameter range.

## originality

PASS

Pass for the varying signed two-hub family, the asymmetric thresholds and the full infinite-leaf law, not for the previously covered positive unit endpoint. The strongest available unweighted-diagonal complete-bipartite statement uses two independent classes and does not state a hub-diagonal parameter tied to the edge coefficient. An earlier formula allowing that parameter would be material; no such statement was established.

## value

PASS

The two adjacent hubs are the minimal split-star modification that introduces triangles and invalidates the sign gauge behind symmetric bipartite bounds. The exact continuum winds up with genuinely different signed positivity thresholds and norm branches and an explicit norming input; the infinite law retains the sign effect rather than erasing it. This is a concrete benchmark beyond the known positive idempotent endpoint and the symmetric bipartite model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
