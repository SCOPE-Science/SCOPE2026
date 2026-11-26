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

The directed maximum is the maximum of adjacent-pair minima and the two one-sided boundary gaps. A mutual edge is precisely an interior strict local gap minimum or a one-sided boundary minimum. In the exact Dirichlet spacing representation with n+1 independent exponential coordinates and their sum S, the interior window counts for a large single gap, adjacent-pair minimum and strict local minimum have site probabilities exp(−u_1), exp(−2u_2) and exp(−3u_3)/3 respectively. There are n−1, n−2, n−3 sites, giving the three exact mean rates with the stated centerings. I checked distinct overlapping windows: adjacent local minima are incompatible; two pair windows need three above u_2, and two nonadjacent overlapping local minima need five above u_3. A single-gap event alongside a pair or triple requires the one above u_1 and one above u_2 or two above u_3. A mixed pair/triple requires two above u_2 and at least one other above u_3. The slowest of these is O(n^(−4/3)); disjoint sites are independent. For an independent confirmation of the no-exceedance limit, partition the exponential coordinates into disjoint blocks of length ceil(sqrt(n)), dropping the O(n/block length) windows crossing cuts, whose total probability is o(1). In each block use the union bound and its second Bonferroni lower bound: summed over blocks, the intersection correction is O(n^(−1/3)) from spatially overlapping sites and O(block length/n) from disjoint sites within a block. The block-hit probabilities have maximum o(1) and sum tending to exp(−x)+exp(−y)+exp(−z); their no-hit product gives the joint CDF. The boundary exceedances are of orders n^(−1/2) and n^(−2/3), respectively, and replacing S by n perturbs every scaled maximum by O_P(log n/sqrt(n)) since the largest exponential is O_P(log n). Thus the three marginal and joint centerings are correct for actual spacings. The uploaded finite checker was inspected but not executed; it is not used to support the infinite limit.

## originality

PASS

The longest-gap marginal, the local-minimum description of mutual pairs, and Poisson machinery are anteceded. The available close papers and catalogue entries address counts, summed spacings, total length, different models, or fewer statistics. The distinct supported claim is the reciprocal maximum's marked-gap extreme scale and its joint independence with the other two centered interval extremes, not the ordinary gap or directed-link marginals on their own.

## value

PASS

The distinction between a long outgoing link and a long mutual link is natural even on a line; mutuality requires a different local event, giving a genuinely shorter leading scale and a nontrivial centering constant. Establishing that all three extremes decouple despite being driven by the same gaps is stronger than deriving separate marginals, and it quantifies how mutuality changes extreme geometry in a baseline sampling model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
