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

The nonnegative symmetric kernel is normalized in each variable. On either side of a unit jump its error has a definite sign, so integration gives twice the cross-cut mass. Integration of the Bernstein basis gives binomial tails with m=n+1, and the tail-sum formula for two independent Bin(m,s) variables yields E_n(s)=E|X-Y|/m. Each of the m Bernoulli differences is symmetric on ±1 with probability u=s(1-s) each and is otherwise zero. Differentiating the product law leaves m times the expected integer second difference of |.|, giving 2m Pr(S_(m-1)=0)>0 for the unnormalized expectation. This includes m=1, and the strictly largest response is at s=1/2. There X-Y has law Bin(2m,1/2)-m; summing positive deviations with (j-m)binom(2m,j)=m[binom(2m-1,j-1)-binom(2m-1,j)] telescopes to m binom(2m,m)/4^m. The signed derivative representation and Fubini bound the error by the integral of jump responses against |Df|. Equality forces |Df| to be supported exclusively at the midpoint, hence exactly the stated nonzero centered jumps plus constants modulo null sets. Stirling gives the stated correction and n=0 gives 1/2. An independently written standard-library calculation (`/workspace/reproductions/bernstein.py`) checked 375 degree/location pairs through n=24, comparing Bernstein antiderivatives with the random walk conditional on its number of nonzero moves and checking the strict midpoint maximum on the test mesh. The universal assertions are analytic, not an inference from that mesh.

## originality

PASS

The supported distinct content is the explicit coefficient at every finite degree and the exact equality family. Same-operator coverage exists for the reduction to a maximum over jump responses and for the asymptotic coefficient/localization. These overlapping claims and the underlying positive-kernel reduction are not credited as new. The strongest historical lead reports earlier sharp one-step work but the available statement comparisons do not establish that the central-binomial coefficient and unique finite-degree extremizer are covered for this kernel.

## value

PASS

The exact coefficient calibrates the intrinsic integrated smoothing error of a canonical positive Markov kernel for every degree, not just the leading rate. The norm is actually attained, and rigidity says that only a centered discontinuity can realize it at any finite degree. Those two finite assertions furnish information that a rate or convergence of maximizing locations cannot supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
