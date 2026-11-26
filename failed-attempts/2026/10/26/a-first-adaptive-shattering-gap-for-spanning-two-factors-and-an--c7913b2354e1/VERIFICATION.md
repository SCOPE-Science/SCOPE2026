---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independent exact enumeration returned 1,3,12,70 labeled two-factors; VC dimensions 0,1,3,4; and Littlestone dimensions 0,1,3,5. For K6 the shattered support counts in sizes 0 through 6 were 1,15,105,395,360,0,0. The Littlestone recurrence over the two nonempty branches of each splitting edge visited 32,853 states for K6. The structural upper bounds also check: any five-edge subset of a two-factor contains vertex-disjoint two-edge paths, and requiring the first path and forbidding the second forces an impossible completion; a depth-six tree would require 32 hypotheses in a positive first branch with only 28. Bridge coordinates are fixed zero and the remaining coordinates give the full disjoint-coordinate product. VC ranks add by restriction and concatenation; Littlestone ranks add by tree concatenation and the fact that at least one branch decreases the queried factor rank. Distinct attachment vertices guarantee maximum degree at most six.

## originality

FAIL

The central finite result has demonstrable equivalent coverage in a distinct indexed result (75fb99d75e09), including the first complete-graph gap with exactly the same concept and query domains. The connected bounded-degree family is not stated there, but follows directly from its K6 entry by adjoining fixed-zero bridge coordinates to a Cartesian product. This is a finding of substantive coverage relative to the inspected catalogue, not a determination of historical priority or an assertion that the Nov 2 entry predates the Oct 26 record.

## value

FAIL

Finding the first gap for a natural spanning class is a motivated exact problem. Here the precise table and onset are already available in the compared catalogue result. The only extra construction attaches fixed-zero edges to otherwise independent hard instances, so it gives no new rank information about genuinely interacting connected blocks. It is useful as an illustration of the gap, but adds only a routine consequence rather than a distinct exact result under review.

The dated certificate retains the supplied scientific assessment, sources and limitations.
