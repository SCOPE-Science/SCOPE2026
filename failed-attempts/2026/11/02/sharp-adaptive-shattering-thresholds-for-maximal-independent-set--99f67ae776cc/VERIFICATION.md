---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independent exhaustive reproduction matched all 24 path/cycle rows of certificate.json and replayed its two witness trees without executing the supplied scripts. Independent plus dominating is equivalent to maximal independent, and the projection-cardinality and first-query minimax tests are exhaustive. P10 has 16 concepts, VC support {0,3,6}, and 16 distinct valid depth-four leaves; C13 has 39 concepts, VC support {0,2,5,8}, and 32 distinct valid depth-five leaves. The counts exclude one further level and the complete support test excludes larger VC supports. Componentwise products add VC dimensions by taking traces, and add Littlestone ranks by concatenation for the lower bound and running the optimal realizable prediction rule separately on each query domain for the upper bound. Paths and cycles exhaust the nonempty connected components; isolates and the empty graph have zero rank. The frozen replay entry points are verify.py and independent_check.py beside certificate.json; their recorded output was inspected, not used as the independent reproduction.

## originality

FAIL

Separate indexed results already state the path and cycle thresholds, and the path comparison gives exactly the disjoint-P10 amplification. The remaining uniqueness statement for all maximum-degree-two graphs through order ten is forced by those two known component tables and product additivity. The October cycle record is broader in the same setting; the distinct same-day path record establishes duplicate coverage without requiring an inference about within-day priority.

## value

FAIL

The smallest-component thresholds are scientifically meaningful in principle, but this submission's headline invariants and amplification duplicate exact records. The only added low-order combination follows immediately from decomposition and additivity. The correct extra replay and table entries do not establish a distinct motivated finding. No valuable repaired claim is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
