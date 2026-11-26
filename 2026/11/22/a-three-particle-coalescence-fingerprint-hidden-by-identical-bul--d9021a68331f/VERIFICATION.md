---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

With r occupied vertices and an individual rate-one clock per vertex, the first holding mean is 1/r and each ordered move has probability 1/(6r). A move to an occupied site decreases r by one. The finite backward system is unique: from every transient state one can force a walk along a path to another occupied site and repeat, giving absorption within a uniformly bounded number of jumps with uniformly positive probability. I reconstructed the graphs and verified the exact integer-scaled means in every one of the 120 pair and 560 triple equations on each graph, without group computation. Classify triples by induced edges and count of common neighbors; the exact total over triples of 112 times the mean is 704960 for each graph. Each has 32 triangles, with respective scaled times 1144 and 1145. The pair values scale to 840 and 1008. This proves the claimed numbers for the finite continuous-time systems; it does not assert equality of laws or extend to synchronous walks. Independent replay: python3 /workspace/check-4.py. Both submitted scripts were inspected, not executed.

## originality

PASS

The inspected sources supply the general coalescence framework, distinct exact observables on the identical graph pair, and voter duality. None supplies these triangle-conditioned means paired with an exact common uniform-triple mean.

## value

PASS

The rook and Shrikhande graphs are natural spectral twins with identical strongly regular parameters. The point of the small difference is not its magnitude: the triangle-conditioned third-particle statistic separates them at an initial shape present 32 times in each, even when the pair means and the entire uniform-triple mean mask the distinction. A precise matched negative control makes the observable comparison useful beyond reporting another pair of numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
