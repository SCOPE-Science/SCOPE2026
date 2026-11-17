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

# Mathematical verification

The proof is the five-step argument in `RESULT.md`, using the exact perfect-graph Hansen facet theorem, rank-one omitted-class restrictions, the strict convexity of the omission barrier, and the Gram determinant lemma. The full claim concerns arbitrary positive integer color-class sizes and every integer count of classes at least two.

The standalone standard-library script `verification/check.py` was run from its packaged path and printed:

`HANSEN_MULTIPARTITE_INCENTER_PASS profiles=32 center_patterns=2520 convexity_inequalities=1770`

It constructs cliques and tests all signed facet inequalities, counts radius-optimal sphere contacts for the complete \(3^r\) grid of box center strata in each tested class-size profile, and verifies the strict scalar omission inequality for \(2\le r\le60\). The checked parameter set is finite: it independently corroborates the derivation but does not prove an unrestricted statement by enumeration.

The radius is a previously published invariant; the center-locus classification, contact count along all of its faces, and intrinsic volume formula are the independently reconstructed claims here. The older Hansen article from 1977 was not completely inspected, so historical-priority certainty and independent scientific audit are not asserted.
