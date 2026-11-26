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

A closed walk of length n with fixed starting index is in bijection with a named feasible cyclic labeling: overlaps recover the columns, and the middle-column test sees all three neighbors of either kind of vertex. I reconstructed all 48,681 edges on 6,561 states in independent Python and synchronously relaxed the integer costs from zero. After ten changing rounds the potential stabilized (range -26 to 0), matching all entries in verification/potential.txt. I checked every reduced cost and pruned the 6,099-edge tight graph by repeatedly deleting sources and sinks. The surviving induced graph consists of exactly seven vertices forming the stated directed cycle, so there is no other tight closed walk. Telescoping gives the bound 7w >= 8n, the cycle realizes equality, and following it from any of its seven states gives exactly the seven distinct labeled minima for every m >= 1. The support intersections per period are one for shifts +/-1 and zero for every other nonzero shift, giving exactly 2m and 3m replacements respectively. This supports the all-order result, not an extrapolation from sizes 7 and 14.

## originality

PASS

The supported distinction is exhaustivity of the seven named minima for all m and the resulting exact reconfiguration graph. The minimum weight and the exhibited word up to shift are already known, so even the existence of seven optima and the exchange distances among those known witnesses are not independent discoveries. No inspected source covers the exhaustivity step.

## value

PASS

The finite certificate resolves a natural all-orders equality-case question for a known sharp domination bound. The result identifies the whole optimum state space and explains why small support moves cannot connect any of the minima as the graph grows; a known weight or sample optima do not tell a reconfiguration researcher this. The support-exchange graph is a useful consequence of the rigidity, rather than the main basis for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
