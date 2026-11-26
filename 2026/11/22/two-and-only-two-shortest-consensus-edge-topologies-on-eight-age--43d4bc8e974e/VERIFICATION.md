---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The 12-contact product for the cube and the Wagner graph was checked with integer entries of the averaging product multiplied by eight. A pure-stdlib Python 3 verifier recursively generates every perfect matching, filters all possible second and third stages by disjoint support, tests each 12-edge support by a backtracking adjacency-preserving isomorphism search, and verifies all 480 admissible cases. Outputs: 12 second-stage matchings of type two four-cycles, 48 of type eight-cycle; 144 schedules with supports isomorphic to the cube and 336 with supports isomorphic to the Wagner graph, zero other. The total is for one fixed first-stage perfect matching, without division by any graph automorphism group.

Analytical checks: the entropy inequality with its equality case, preservation of support ratios, forced equal support sizes, the three-stage reduction, and the almost-sure occurrence of a successful word for independent contacts drawn from a fixed full-support law. The checker verifies the finite classification, not bibliographic priority. The deterministic result does not classify longer protocols.
