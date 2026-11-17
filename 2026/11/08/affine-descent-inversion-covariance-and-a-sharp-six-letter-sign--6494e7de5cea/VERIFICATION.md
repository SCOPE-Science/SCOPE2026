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

Uniform multiset words are exchangeable sampling without replacement. The local descent probability is p=T/[n(n-1)]. Adjacent swapping decreases total inversion count by one without altering unrelated pair contribution; reversing the word maps I to T-I and D_i to ascent at n-i, giving mirror c_i+c_(n-i)=p. Replacing an earlier third position by a later one changes the covariance by the average of sign(C-A)+sign(C-B) conditioned on A>B; triple-distinct label terms cancel and tied third copies contribute numerator S. Thus constant slope S/[n(n-1)(n-2)] and the affine formula follow for all n>=3. Summing i c_i yields (3T+S)/12; |S|<=(n-2)T proves nonnegative through size five. At n=6 S<-3T is possible uniquely for ordered (5,1), giving -5/12. Direct exact rational enumeration reproduces (5,1) value, and n=2 case is separately handled. The infinite bound is algebraic, not an extrapolation from the checker.

## originality

PASS

Thiel gives a genuinely broader exact inv/maj bivariate recurrence and leading mixed asymptotic moments, while Conger–Viswanath gives inversion/descent marginal/joint indicator ingredients. Such generating formulas permit derivative computations but neither inspected primary statement explicitly states the finite position-resolved affine covariance kernel, its exact signed S term or the unique first negative six-letter ordered profile. The result is a sharp extracted qualitative dependence theorem, not the invention of a new multiset statistic. Priority risk: derivatives of previously published recurrence may make its aggregate covariance straightforward and implicit; no claim of novelty for the raw generating function.

## value

PASS

The dependence of inversions on each individual descent location is a natural fine statistic for random permutations with ties; the affine signed covariance profile is an all-size structural identity and yields a sharp sign-transition classification. The first negative covariance between equidistributed major-index and inversion statistics at length six with a unique ordered multiplicity profile is a meaningful exact boundary, not a numerical table alone or a rename of a known mean. It is independently useful for finite-sample dependence questions despite prior methods for generating moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
