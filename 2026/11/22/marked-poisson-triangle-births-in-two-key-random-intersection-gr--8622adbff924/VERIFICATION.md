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

For three pairwise intersecting two-sets without a common key, the sets must be the three distinct edges on three keys; this yields the exact probability 6 binom(m,3)/binom(m,2)^3 for an ordered sample triple. The respective union bounds for such a cycle, a key with at least four appearances, and three identical sets are O_b(m⁻¹), O_b(m⁻¹ᐟ³), and O_b(m⁻²). On the complement the triangle/third-key bijection holds simultaneously for every prefix, with the same birth index. In the iid two-slot coupling, resampling collisions within pairs changes a prefix of n vertices with probability at most n/m. A rate-two labelled clock splits into independent rate-2/m clocks; the third-time CDF at t m^(2/3) is 4t³/(3m)+O_b(m⁻⁴ᐟ³), uniformly for bounded t. The independent Laplace products and label-grid sums give intensity 4t² dt du. A hit at slot k is assigned to vertex ceil(k/2), so the uniform maximal discrepancy from the corresponding Poisson arrival over O_b(m^(2/3)) slots is o_P(m^(2/3)). Near zero, the expected number of original keys hitting three times by εm^(2/3) is at most m binom(floor(εm^(2/3)),3)(2/m)³ ≤4ε³/3; thus the locally finite limit loses no initial jumps. The limit has no fixed boundary atoms or time ties, so convergence on [0,b] transfers to J1 for the counts. The first-event assertion follows by taking b large, since the limiting survival at b is exp(−4b³/3), and the intensity factors in time and label. For the quantitative claim, comparing a=2n iid slots with K of law Poisson(a) changes the third-hit count with probability at most m⁻² E[|K−a| binom(max(K,a),2)] ≤ O(m⁻²√a(1+a)²)=O_b(m⁻¹ᐟ³) by Cauchy–Schwarz, also valid at a=0. The Poissonized count is binomial with success q=Pr(Poisson(a/m)≥3)=O_b(m⁻¹); Le Cam gives O_b(m⁻¹), and expansion of mq plus integer rounding gives a mean mismatch O_b(m⁻¹ᐟ³). These errors combine with the graph and pair couplings and bound one-time TV uniformly in t, not path TV. The frozen VERIFICATION.md and verify.py were inspected without execution; their finite checks do not certify the asymptotics.

## originality

PASS

The scale and the common-key contribution are already in random-key-graph theory, and the first-third-hit Weibull law is inherited birthday theory after changing from draws to vertices. The supported increment is the transfer to the full key-marked graph birth process with a simultaneous unique witnessing key and the explicit uniform bounded-horizon one-marginal TV estimate in the fixed-two-distinct-keys graph. The elementary Poisson embedding or the first-event time law in isolation is not the novelty claim.

## value

PASS

The result turns a triangle threshold into a process law and explains which triangles cause it and when they appear. The simultaneous witness property rules out extra motifs and multiple witnesses throughout a bounded critical history. The one-time error estimate quantifies performance in the original fixed-size graph, rather than only for an occupancy proxy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
