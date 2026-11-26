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

For independent singular rank-class factors, choosing an independent uniform admissible domain and uniform signed permutation gives uniform maps: a fixed rank-r partial bijection has 2^(n−r)(n−r)! extensions. Intersect the domains after pulling each back by the preceding full permutation product. Conditional on all the permutations, these pulled-back domains are independent, with unchanged uniform laws, hence independent of the terminal full permutation. It follows that the product is uniform conditional on attained rank (by symmetry of the intersection and uniformity of the terminal extension). Counting j-subsets of this intersection gives the stated binomial moments: there are 2^j binom(n,j) admissible j-sets and the single-factor inclusion probability is binom(r,j)/(2^j binom(n,j)). Binomial inversion then gives the exact prescribed-target counts and independence of the order of the rank parameters, including k=1 and rank zero. Units cannot arise. For maximal singular rank, each pair contributes one independent sign-agreement event of probability 2^(−(k−1)); the rank is binomial. Zero is absorbing. Tail-summing with S=T−1 and expanding 1−(1−2^(−t))^n gives the expectation with the initial +1. Along the specified subsequences n times the survival parameter tends to 2^(theta−z), giving the lattice-phase CDF. The two-factor formula separately counts t agreements, j opposite-sign selections in occupied pairs, and the remaining free signed-pair choices; the factorial moments give the displayed eigenvalues.

## originality

PASS

The distinct content is the evaluated signed-admissible product law on all singular rank classes and its dyadic maximal-class absorption. The strongest unsigned inverse-monoid comparator already gives the same kind of uniform-extension mechanism, target-specific product law and commutative rank algebra for ordinary subsets. Embedding a signed partial map in the ordinary rook monoid on 2n points does not identify the measures: for r≥2 admissible rank-r inputs exclude the domains meeting an opposite pair twice. In particular ordinary full-support or fixed-cardinality thinning does not give independent per-pair sign agreement. The inspected general inverse-semigroup or monoid Hecke results do not compute the admissible intersection probabilities. Neither elementary monoid cardinalities nor the extreme-value limit form by itself is claimed as new.

## value

PASS

This evaluates an exact convolution invariant of a classical family: every prescribed output fiber for arbitrary singular rank profiles and word lengths, not only the monoid's size or expected rank. The dependence imposed by opposite pairs changes the thinning and absorption mechanism compared with unpaired subsets. The resulting binomial thinning and the full phase-dependent zero-time law are natural consequences of the evaluated product structure, rather than an unrelated numerical example or a new claim about generic extreme values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
