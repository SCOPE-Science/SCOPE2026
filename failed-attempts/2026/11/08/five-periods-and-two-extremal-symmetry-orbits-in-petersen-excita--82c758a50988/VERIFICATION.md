---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS: Independently generated adjacency from disjoint two-subsets and computed all 3^10=59049 exact successors under all four update cases. Full functional-graph traversal reproduced every t=0..6/period 1,3,4,5,8 cell, all 120 maximal-delay states, orbit counts, and F^126=F^6. Independently enumerated all S5 actions on both extremal representatives, obtaining two disjoint orbits of 60 exhausting the maximal-delay set. Finite computation IS exhaustive of the finite stated domain; no extrapolation to graph families.

## originality

FAIL

FAIL: A full earlier theorem from 2026-11-02 plus its exact machine-readable full first-entry/period table completely covers the same Petersen dynamics; new two-orbit delayed-state presentation is straightforward postprocessing of earlier exhaustively enumerated state map under the known S5 automorphisms.

## value

PASS

PASS for the underlying object/invariant: Petersen is a canonical cubic graph and full first-entry/period and S5-extremal-state classifications are natural dynamical invariants, not random trajectory samples. The present package is nonetheless redundant with a published full census, so it is rejected for originality; no claim that reproduction itself is a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
