---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The two formal recursions correctly mark a root by depth parity, and mark an empty ordered child list by y. For n≥2 the two marginals coincide by the displayed quadratic and are Narayana with parameter n−1, giving mean n/2 and variance n(n−2)/[4(2n−3)]. Independently, setting λ=z/(1−T)^2 and η=2z/(1−T)^3, the mixed derivative satisfies (1−λ²)F_xy=F_y[1+2ηλF_x], with F_x=T/(1−λ²) and F_y=z/(1−λ). Substitution of T=(1−s)/2 gives the displayed Laurent polynomial in s. Its coefficient for n≥3 divided by C_(n−1) gives E(EL)=n²/4−n/[4(2n−3)]. Another check: with e even vertices and o=n−e odd vertices, Lagrange inversion factors the offspring-weight enumerator as (1/e)[t^o]A(t)^e [t^(e−1)]B(t)^o. The conditional expected leaf count is therefore e(e−1)/(n−1)+o(o−1)/(n−2); its odd part in e−n/2 is −(e−n/2)/(n−2). The marginal is symmetric, so the covariance is −Var(E)/(n−2), giving the same answer. The unique n=2 tree gives zero variance and undefined correlation; n=3 gives perfect negative correlation. A fresh bounded Dyck-path enumeration (semilength n−1; count peaks for leaves and up-steps to even height plus the root for even vertices) matched the moments for n=2,…,8. The frozen script was inspected but not run.

## originality

FAIL

Mallows–Wachter (1972) already give the bicolored valency enumerator together with a decomposition by the root's valency. Both the exact pair and the frozen two-type generating system are direct specializations, after the explicit root correction below. The published article need not print the rational covariance for this to be genuine coverage. Common Narayana marginals alone do not imply it.

## value

FAIL

The negative covariance and small normalized correlation are sensible descriptions of the coupling, but the frozen claim extracts them by standard differentiation from a specialization of an existing exact bicolored valency enumerator. There is no independent structural result in the frozen contribution beyond that extraction and the classical marginals. No genuine surviving repair is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
