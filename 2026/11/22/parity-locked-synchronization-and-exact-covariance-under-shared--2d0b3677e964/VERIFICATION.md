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

For the aligned lattice of the isotropic quadratic, one can label the equally probable noise cells by j=1,...,2m so that k moves up iff j>k. For k<l, precisely l−k cells move them toward each other; if adjacent this swaps them. Hence gaps decrease by two until 0 or 1 and have independent geometric holding times at their successive levels, including deterministic or zero waiting-time edge cases. Within any initial parity class two indices cannot cross without meeting; its initial extremes therefore determine its entire coalescence time. Once both classes have coalesced and their representatives are adjacent, the lower index L moves up or down with counts 2m−1−L and L, respectively, and the class order flips with count one. The binomial weights on L satisfy neighboring detailed balance and the fair order satisfies flip balance. The recurrent set is irreducible; parity alternation and a positive two-step return give period exactly two, also for m=1. The variance follows by writing the centered average as the centered L plus (2r/d−1) times the centered fair Bernoulli, scaled by δ. The independent-noise product law need not be the only invariant law, because of parity phases; the cited independent-noise variance nonetheless holds under the product law and within any relative-parity recurrent class after averaging both phases, since the parity-conditioned binomial means both equal m. It is not an ordinary-time convergence result. Fresh exact-rational checks covered every ordered pair for m=1 through 5 and invariant mass and average variance for three four-coordinate class-size patterns.

## originality

PASS

The defensible distinct content is the full common-uniform joint kernel and its quantitative parity-locked hitting and invariant laws, not the already known binomial marginal or generic signSGD update. The inspected scalar and coupling statements do not determine this common-threshold joint law.

## value

PASS

The model isolates a concrete failure of dimension-based variance reduction without changing curvature or marginal noise: perfect dependence collapses arbitrarily many variables to at most two classes and produces an exact stationary covariance penalty. The distribution of the settling time and the comparison at fixed marginals make it useful as a precise benchmark, not as a general claim about signSGD on arbitrary objectives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
