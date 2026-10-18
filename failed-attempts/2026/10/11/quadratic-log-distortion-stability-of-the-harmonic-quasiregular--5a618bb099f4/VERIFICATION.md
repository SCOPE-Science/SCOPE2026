---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Read the entire displayed coefficient C(K), k and L(K) in arXiv:2609.33140v1 Theorem 1.5. With c=cosh((log K)/2), s=sinh((log K)/2), k=s/c, L=2c/(1+c), the product (kL/2)*s=(s²)/(1+c)=c-1 exactly. Hence C(K)=C0 c+(c-1)(3sqrt3/2+coth(2c/(1+c))). Derivative in c is C0+A+coth(ell)-2(c-1)/(c+1)^2*csch²(ell)>C0+A+3/4>0 because ell>=1 and 2(c-1)/(c+1)^2<=1/4. c=1+q²/8+O(q4) gives exact alpha=(C0+A+coth1)/8=0.69887946077..., no odd term. No claim of fixed-K optimality follows.

## originality

FAIL

The paper already publishes the *entire explicit function* C(K) for every K>=1 in Theorem 1.5, in precisely the same harmonic quasiregular setting. The new profile is an exact invertible hyperbolic substitution and the first ordinary Taylor coefficient and derivative sign of that known elementary expression. The stronger pointwise formula already determines the claimed asymptotic and monotonicity without a new estimate, invariant, or extremizer; absent a substantive new theorem, these are covered corollaries of the published global formula.

## value

FAIL

The observation that the already supplied C(K) has vanishing first derivative at K=1 is mathematically correct, but follows by a routine two-term Taylor expansion of an explicit published coefficient; it does not establish a new sharp fixed-K stability bound, new extremal phenomenon or any unknown natural invariant. Its isolated 0.698879 coefficient is derivative data mechanically supplied by the earlier exact formula, below the stated substantive-value threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
