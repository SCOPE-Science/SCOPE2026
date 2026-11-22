---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The frozen source specifies all nine vertices, ten arcs, initial chip vectors, and deterministic simultaneous firing recurrence. Exact whole-state recurrence detects first repeats after 5 or 9 states and generates 5,8,7,6 maximal firing sets for h=0..3. Covering their downward-closed face complex by full maximal simplices has contractible finite intersections; the nerve lemma applies. Direct nerve enumeration yields 20,129,75,39 faces and deterministic elementary free-face removals 7,45,37,19. Reduced h0 nerve is a 3-edge circle and h2/h3 each a vertex. For h1 the remaining 8 vertices/18 edges/13 triangles carry 11 explicit edge-triangle Morse pairs and a complementary seven-edge spanning-tree matching; inspecting the code confirms acyclicity via complete reversed Hasse DAG, with exactly one critical vertex and two triangles, which is an integral wedge S2veeS2. Independent recurrence and bitset homology matched all four phases. Finite proof is exhaustive for four specified configurations only.

## originality

PASS

Riihimäki–Smith 2026 primary article establishes avalanche complex framework and synchronized-symmetric two-cycle wedge case (symmetric h=0); its discussion of asymmetric wedge cycles does not classify the shifted six-chip configurations h=1..3. Resultary near-critical directed rose sphere and separate-cycle gcd results use different chip regimes/graphs and do not imply the exceptional two-2-sphere phase. Full prior coverage acknowledged for h=0, while all three shifted cases are original best-of-knowledge.

## value

PASS

This is a complete exact finite phase diagram for a minimal natural directed rose, showing a geometrically nontrivial transition from circle to two two-spheres to contractibility as just one vacancy moves. The two-sphere multiplicity and subsequent disappearance motivate studying asynchronous mixed-cycle avalanches; it is a meaningful non-obvious boundary classification, not a random bit pattern.

The dated certificate retains the supplied scientific assessment, sources and limitations.
