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

For alpha>=2/3, first floor(3alpha)>=2 excludes 1. For 1/2<alpha<2/3, write floor(alpha(2^n+1))=2^(n−1)+floor(2^n(alpha−1/2)+alpha), let N be first positive excess, then 2^(N−1) is unrepresentable. For alpha=2^-k the nonzero floors are binary powers 1,2,4,... and give full coverage. Exact identity H_n=1+alpha(n−3)−sum_{j<=n}{alpha(2^j+1)}+{alpha(2^(n+1)+1)} follows from sum_{j<=n} s_j−s_(n+1)=n−3. If H_n<0, the entire interval (sum floors+1,..., next floor−1) is absent; intervals disjoint. For h!=0, ∫_0^1 |N^-1 sum_{j<=N}exp(2pi i h 2^j alpha)|²dalpha=1/N by orthogonality; Chebyshev and Borel–Cantelli along N=k² plus interpolation imply a.e. Weyl equidistribution, fractional mean 1/2, H_n/n->alpha−1/2. Independently checked 39 exact rational H_n identities. Finite checks do not imply a.e. theorem.

## originality

PASS

Wu–Ma 2026-10-28 supplies existence of some strongly complete scale at critical inequality s_(n+1)<=2s_n, not the measure or a.e. missing-gap law for this particular strictly subdoubling sequence. Ma–Chen 2022 positive measure assumes fixed gamma<2, and its published full text could not be accessed; abstract only. Earlier published SCOPE exact doubling-tail binary carry budgets applies only to *eventual exact equality* s_(n+1)=2s_n, not (2^n+1). No checked published theorem implies the present measure-zero counterexample or explicit linear gap coefficient. Qualified priority remains.

## value

PASS

Shows the sharp failure of a positive-measure extension when one replaces uniform ratio gamma<2 by every-point strict ratio<2, despite existence of infinitely many complete scales. The a.e. linear missing-gap coefficient is a quantified natural boundary phenomenon, not just a cheap negative example or random slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
