---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The supplied connected six-vertex graph, 0/2 BR and 1/3/4/5 imitators, strict opponent-coordinate payoffs and specified 10-switch word were independently recalculated from all integer edge payoffs. Each of ten updates changes the indicated bit, each imitation has exactly one maximum-earning neighbor and each BR improves strictly; after 10 switches the initial six-bit state is reached. Vertex 5 has an idle activation at that state; adding it at the start gives a repeating length-11 activation word visiting all six vertices each period. Thus deterministic fair non-equilibration is a complete finite existential proof for *neighbor-only* imitation, not an assertion about random schedules or own-payoff threshold rules.

## originality

PASS

The explicit six-vertex graph and integer payoff table do not appear identical to the earlier four-vertex certificate, so the six-agent exact configuration itself may be original. But the main claimed general-graph consequence, refutation of universal convergence/potential for persistent mixed dynamics, was decisively established by an earlier smaller four-agent fair periodic example in the same model. Originality PASS is strictly qualified for the precise six-agent witness, NOT for that already-known negative general theorem.

## value

FAIL

FAIL. The six-agent ten-switch certificate is a correct reproducible example but the source gives no mathematical need for exactly six agents, four imitators, two best responders, or ten switches, and explicitly disclaims minimality. A previously documented four-agent fair periodic orbit already refutes universal convergence on connected coordinating mixed networks, and the earlier formal orbit uses strict best-response moves and uniquely maximizing imitator neighbors on effective steps. Merely producing a larger, less sharp counterexample without a new natural invariant, threshold, minimality, robustness principle, or motivated constraint does not establish incremental mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
