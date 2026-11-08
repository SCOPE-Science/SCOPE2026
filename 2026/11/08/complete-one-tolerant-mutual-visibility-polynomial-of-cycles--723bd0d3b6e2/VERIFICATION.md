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

# Verification

Run `python3 verify.py` with standard Python 3 from this directory. The script requires no input files or third-party modules. It constructs all shortest clockwise and anticlockwise paths between chosen vertices of labelled cycles and directly checks the ordinary one-tolerance condition. It exhaustively enumerates all subsets for every \(3\le n\le18\), including both shortest arcs at antipodal pairs. In a separate computation, it enumerates every positive cyclic composition into four and five gaps for \(5\le n\le32\) and checks against the closed formulas. A successful run prints `GEODESIC_EXHAUSTIVE_OK` for each tested order, `CYCLIC_COMPOSITION_CHECK_OK 5..32`, and `VERIFY_OK`.

## Logical checks

The unrestricted proof bounds the degree by five and uses a necessary-and-sufficient gap criterion for each nontrivial cardinality. For five selected points, violation events indexed by the five gap pairs have only adjacent-pair intersections, so exact inclusion-exclusion terminates at order two. Closed-form expressions for single and adjacent-pair events are proved algebraically, not inferred from tests.

## Limits

Only the displayed finite test orders have been exhaustively computed; the arithmetic checks alone do not prove the infinite theorem. Independent audit has not been performed. The known degree-five extremal fact is distinguished from the new coefficient identities.
