---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The theorem is mathematically true in the stated domain. Huang Theorem 2.7(2) proves the uniform upper bound. Theorem 2.3 yields exact fixed-diagonal error multiplication by λ=1-c0/c: any nonfixed off-diagonal initial perturbation gives root rate |λ|. Eq. (2.15) for normalized diagonal p gives p_k=p0^(r^k), r=1-1/c; for p0!=1 and r!=0 the entry error equals (log p0)r^k+O(r^(2k)), yielding root rate |r| regardless of off-diagonal dynamics. For r=0, diagonal mode root rate 0; for λ=0 the other witness suffices; for c0=c=1 the source upper bound forces zero rate. Thus the worst rate is max(|r|,|λ|). With s=1/c in (0,2/c0), c0>=1, s*=2/(1+c0) lies inside this interval. For s<=s*, F(s)>=1-s>=1-s* and for s>=s*, F(s)>=c0*s-1>=c0*s*-1, both strict except s=s*. Hence the unique optimum and formula. Matrix norm equivalence does not alter root rates. Independent rational-grid checks only corroborate these arguments, not prove universality.

## originality

FAIL

The 29 September 2026 primary paper already proves the two exact mode dynamics, the global root-rate upper bound, and c0>=1. Its Theorem 2.3 supplies the exact fixed-diagonal scalar contraction 1-c0/c, Theorem 2.7(1) and proof (2.15) supply the exact diagonal law p_k=p_0^(1-1/c)^k, and Theorem 2.7(2) supplies the matching global upper bound. Choosing a nonfixed initial point in each separately invariant witness family makes both terms sharp by elementary limit manipulation. The claimed exact worst-case factor is therefore an immediate corollary of the earlier proven results. The displayed optimum is then the standard two-affine-factor Chebyshev/Richardson balance s=2/(1+c0), a one-line exact minimax calculation. Absence of the final displayed formula in the earlier paper is not originality; all exact claims are already implied by its proved statements.

## value

PASS

The constant relaxation denominator is an intrinsic algorithmic design parameter and the exact robust convergence factor is a natural invariant over all starts. Unlike the source's one-step choice c=c0 for fixed diagonal, the optimal global choice c=(c0+1)/2 genuinely balances distinct diagonal/off-diagonal decay modes. For example, when c0=5, the robust rate improves from 4/5 at c=5 to 2/3 at c=3. A user of the iteration could need the sharp setting; no downstream theorem is required for that practical mathematical question. Nevertheless its modest algebraic difficulty and direct implication from earlier exact recurrences bar originality; V is not asserted on the basis of novelty or testing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
