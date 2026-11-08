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

# Verification record

The companion `verify.py` is a standalone Python 3 standard-library program. Its execution after extraction from the saved package completed with `PASS 8112 exact rational assertions`.

The checker independently enumerates every parent–incident-hyperedge event at each finite state, checks all transition rows sum to one, and separately evaluates the derived edge-count drift. It checks neutrality, strict drift, and the ordinary-graph equality boundary. For every listed example on at most five vertices, it solves the complete rational absorption equations and compares every mixed state's fixation probability with the exact Moran benchmark. The complete-three-uniform four- and five-vertex one-mutant probabilities also reproduce equations (20)–(21) of Liu and Masuda (2023).

Tested hypergraphs: single groups on three and five vertices; complete triples on four, five and six vertices; cyclic triples on five and six vertices; all triples and quadruples on five vertices; and the ordinary five-cycle graph. Fitness values tested were \(1/2\), \(2/3\), \(1\), \(3/2\), \(2\), and \(4\). These are finite consistency checks, not certificates for all population sizes. The analytic convexity and finite-state stopping argument establish the unbounded theorem.

No external or independent audit has been performed. The verification does not address unindexed publication priority, irregular hypergraphs, time to absorption or alternative update rules.
