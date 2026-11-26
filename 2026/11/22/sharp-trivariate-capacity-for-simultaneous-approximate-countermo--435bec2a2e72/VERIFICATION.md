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

For each i the centred coordinate satisfies 2Xi=(Xi+Xj)+(Xi+Xk)−(Xj+Xk). Thus success projects into a central interval of length at most 3ε; the one-dimensional marginal gives the upper bound for every Borel coupling, including at ε=0. Independently normalize to ε=1/3: for T uniform on [0,1], randomly permute ((5+T)/6,(3−T)/6,(1+T)/6), with independent equally likely simultaneous reflection. The three raw pair sums are 4/3, 1+T/3 and 2/3; reflection preserves the tolerance. The six affine marginals range over the six successive sixths, each selected with probability 1/6, so each mixed coordinate is uniform. For 0<ε<1/3 scale this successful coupling toward 1/2 by 3ε and assign it precisely the marginal mass 3ε of the resulting interval. On the complementary branch take uniform marginals on the two outer parts; this branch cannot succeed by the projection bound. The threshold coupling works unchanged above 1/3. The inspected rational diagnostic is finite and not needed for this continuum proof.

## originality

PASS

No distinct source located gives the exact three-slab probability or implies its attaining coupling. The identical catalogue entry is the assigned result, not independent corroboration or independent prior coverage. The closest distinct catalogue statements optimize geometrically different events; literature-access limits make the conclusion provisional rather than a priority certification.

## value

PASS

This is a natural quantitative relaxation of mutually incompatible pairwise antithetic requirements. The projection bound alone does not show that three marginal requirements can be saturated by the same law. The piecewise-affine attaining coupling gives the exact attainable guarantee and feasibility threshold, useful for bounded-error dependence design and as a benchmark for multistochastic event optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
