---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For the continuous-time SIR process with one infectious seed and homogeneous edge rate beta, event-clock conditioning gives an acyclic recursion for expected absorption time h and expected subsequent infections f. Independently recomputed every graph–missing-edge–seed triple on n<=3: exactly 38 labeled cases, with symbolic nonnegative differences for all beta>0, including disconnected graphs. For a four-cycle with edges 02,03,12,13 and seed 2, inserting diagonal 01 at beta=10 changes mean duration by -1631125/648015984 and expected final infections by +8200/586971; exact-rational independent computation matched both. This is a witness at n=4, not an exhaustive four-vertex classification. It uses mathematical coefficient positivity, not finite beta sampling, for the all-rate lower bound.

## originality

PASS

On a best-of-knowledge comparison of exact claims and stronger implications, no inspected prior source determines the complete submitted theorem. Known premises and specialized coverage are credited; the precise remaining potential overlaps are listed as residual risks.

## value

PASS

A sharp counterexample to intuitive contact-addition duration monotonicity is meaningful: greater final epidemic size need not mean longer epidemic duration. Four vertices is a natural minimal boundary and the exact witness is relevant to stochastic network-process comparisons, independent of general CTMC computability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
