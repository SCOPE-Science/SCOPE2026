---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and finite proof certificate

Running `python scripts/build_census.py` from this directory verifies complete state-by-state agreement of two separate implementations for all eight local bias policies and reproduces `certificates/census.json`. The executable domain is precisely all 2048 binary words of length eleven per policy. The finite proof has no probabilistic sampling, skipped states, external libraries or unresolved computations. No direct infinite-dimensional conclusion follows from these finite results.

The checker `scripts/peeling_certificate.py` constructs the entire functional digraph by bit masks derived from an independent edge list. Iterative zero-indegree removal leaves precisely the cycle nodes. Reverse peeling order determines entry depth and attracting representative for every vertex. The second checker `scripts/direct_walk.py` uses an explicit adjacency list, separate transition routine, and direct first-repeated-state detection; the complete multisets of basin sizes and first-entry/period pairs agree. `scripts/build_census.py` checks equality and serializes all counts. The action of the two explicit adjacency-preserving permutations on the degree-four sites supplies symmetry reduction, which is also checked by evaluating every bias subset rather than assuming it.

This verification is a mathematical finite exhaustive check, not independent external validation or a certificate about historical novelty.
