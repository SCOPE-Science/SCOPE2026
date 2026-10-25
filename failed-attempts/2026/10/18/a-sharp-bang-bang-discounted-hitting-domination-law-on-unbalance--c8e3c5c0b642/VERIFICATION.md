---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Two-equation symmetry reduction is exact: unpinned side potentials U,V depend only on counts (q,r), with determinant 1-lambda^2(1-s)(1-t)>0. The feasibility polynomial counts all labelled pinned choices by binomial weights; saturated parts have opposite-side hit potential lambda. In s>=t half-plane, u>=tau forces s>=f(t) with f strictly decreasing and concave for tau<lambda, so the linear cost is bounded below by the smaller endpoint costs a min(1,rho) and (a+b)beta; reverse half-plane is no better since a<=b. One-sided rounding attains ceil L; balanced rounding attains <=ceil L+1; tau=lambda and >lambda boundaries follow from one-step cap. Independent exact occupancy enumeration for K_{3,4}, lambda=1/3,tau=1/8 gives L=2, optimum=3 and 31 optimal sets in (1,2),(2,1),(3,0) profiles 18,12,1. Comparison rho/beta=(1+lambda)/lambda gives the claimed aspect-ratio threshold. The result is internally correct, including sharp +1 witness.

## originality

FAIL

FAILED: a publicly available earlier theorem, Exact discounted hitting domination of complete bipartite graphs (published 2026-10-04), already treats every K_{m,n} including all the submission’s unbalanced cases and gives the exact least feasible occupancy b_a for each a in elementary ceiling formulas. This pointwise characterization immediately determines every feasible (a,b) and every binomial-weight coefficient of the submitted all-set polynomial, and its minimum is the very optimization objective. The new +1 approximation and continuous phase characterization may offer explanatory inequalities not explicitly worded in the older result, but the central optimum/profile claim is prior-covered; they do not restore novelty of the submitted combined full theorem as presently framed.

## value

PASS

The continuum one-sided/balanced transition and sharp additive-one integrality gap offer genuinely interpretable structural information for a natural graph family; however a formerly unknown exact optimizer cannot be claimed since a stronger earlier all-profile formula exists. This explanatory mathematical value does not override the originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
