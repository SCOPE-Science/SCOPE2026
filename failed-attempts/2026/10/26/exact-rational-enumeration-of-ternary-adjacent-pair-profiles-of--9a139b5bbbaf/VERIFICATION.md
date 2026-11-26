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

A nonempty profile has a realizing word exactly when its directed multigraph is weakly connected on the active vertices and has balanced degrees or a single start/end imbalance. Disconnected loop components cannot be repaired by loops. On three active vertices, the signed oriented multiplicity differences are (t,t,t) for closed trails or (t+1,t,t) for one prescribed open direction, up to permuting the symbols. Each matched pair of opposite arcs contributes 1/(1-z^2). The minimum cross-length in the open class is 3t+1 for t>=0 and 3|t|-1 for t<=-1, giving the displayed two numerators. Subtract the zero or single-pair supports as appropriate, then add arbitrary loops on the active vertices; the source formulas count every profile once. The empty length-one profile is counted once. Exact rational simplification matches the displayed fraction; its dominant pole has order seven and multiplier 7/12, giving 7/8640 after coefficient extraction, with all other poles of lower order. The maximum observation-separating code cardinality is one word per realized profile.

## originality

FAIL

The distinct same-day support-refined cyclic-profile result already gives a bivariate exact enumerator from which the frozen all-length linearly observed count follows by a direct bijection and one derivative. This is demonstrable statement-level coverage, independent of within-day priority. Separately, the leading coefficient is implied by the earlier published asymptotic comparison and was correctly not claimed as new. Two exact later catalogue matches confirm the mathematical overlap but are not used to assign earlier priority.

## value

FAIL

The exact ternary observation count is natural and its coefficients matter for exact code capacities. The frozen record, however, adds no independently unresolved invariant beyond the projection of the complete cyclic support series. Its asymptotic coefficient and the one-representative code interpretation are already immediate consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
