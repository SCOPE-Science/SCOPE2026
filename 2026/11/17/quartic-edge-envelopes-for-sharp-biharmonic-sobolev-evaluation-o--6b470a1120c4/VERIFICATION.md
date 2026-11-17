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

# Reproducibility of the quartic biharmonic evaluation result

Run `python check_biharmonic.py` with Python 3 and SymPy installed. This script uses **exact rational arithmetic**, constructs the Kirchhoff vertex Green function and integrates quadratic edgewise restrictions exactly. For verification independent of the formula being checked, it subdivides each test edge at four different rational interior coordinates and re-solves the **new, larger graph's** vertex equations for a delta source at the new subdivision vertex. It compares the resulting integrated squared Green function against the proposed edge polynomial.

Actual execution yielded:

```
TWO_EDGE_METRIC_CIRCLE_CONSTANT_PASSED
FOSTER_CYCLE_RANK_QUARTIC_SUMS_PASSED 10
INDEPENDENT_SUBDIVIDED_GRAPH_GREEN_COMPARISONS_PASSED 140
EXACT_BIHARMONIC_QUARTIC_LEADING_COEFFICIENT_PASSED 35
EXACT_INTERVAL_NEUMANN_BIHARMONIC_EXAMPLE_PASSED
ALL_BIHARMONIC_ENVELOPE_CHECKS_PASSED
```

The graph cases include an interval, a metric circle represented by two parallel edges, unequal-edge paths, a weighted triangle, a star, a graph with overlapping cycles, a cactus, and three pseudorandom connected rational-length networks with deterministic seed. The leading coefficient test independently solves the unit-current effective resistance network and compares against the fourth-degree coefficient. The interval example verifies the exact expression \(Q(x_t)=1/45-t^2(1-t)^2/3\) at unit length.

**Limits:** A finite collection of rational tests cannot establish the identity for all positive real edge lengths or all graph topologies. The universal proof instead uses the exact moving-source Green identity, polynomial integration, self-adjoint spectral theory, and the electrical trace/Foster identity. No independent audit has been performed.
