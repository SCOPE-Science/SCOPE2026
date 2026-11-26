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

Corollary 13 of Angel–Goldschmidt–Michaeli supplies the required lower maximum-speed bound at a=0, for the same pinned Gaussian increments and all vertices. At each birth the conditional mean depth profile multiplies by 1+z/(j−1), giving the expected product. Tilting by exp(η) completes the square independently at each edge and multiplies its weight by c=√e, making the normalized annealed depth PGF a product of Bernoulli PGFs with probabilities c/(t+c). Its normalization is Θ(n^c), and a fixed relative depth error has probability n^{−a} for some a>0. For k between c log(n)/2 and 2c log(n), bounded mark averages, Gaussian centered partial-sum maxima and squared marks (using their finite exponential moment near 0) all have exponentially small error probabilities on the log(n) scale. Thus the expected number of bad paths ending above (c−ε)log(n) is O(n^{ε−a}) for ε chosen after the error tolerance. The maximum lies above that level with probability tending to one. A countable convergence-determining class gives weak convergence in probability; Gaussian continuity at zero gives the sign fraction; the uniform profile follows by the depth limit and a rounding error of order 1/log(n). The zero-depth event vanishes; distinct vertex differences are nondegenerate conditionally on the tree. The frozen finite checker was inspected, not run, and is not needed for the analytic identities or the limit.

## originality

PASS

The maximum speed and the change-of-measure framework are prior work, and the depth scale had already been predicted. The supported distinct result is the joint annealed first-order ancestral limit for the actual fixed-population maximizer, including an unbounded moment and uniform path assertion, not the speed or the Gaussian tilt in isolation.

## value

PASS

This resolves a same-model extremal-depth heuristic and quantifies how the actual maximizing ancestry differs from an ordinary root path. The nonzero negative-increment proportion and uniform profile give information an endpoint speed cannot provide, and the separate second-moment control rules out a conclusion based solely on a weak empirical law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
