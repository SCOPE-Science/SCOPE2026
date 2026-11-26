---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The disjoint prefix-sibling pairs give the lower bound because their strict predecessor layers agree. Exactly one completion of each prefix satisfies the orientation rule, and no alternating word does. The one- and two-step layers are disjoint; the only possible center overlap is the period-two case, which is unselected. At odd length the two selected second predecessors give the unique repeated length-(n-2) suffix; the unique sensor with that suffix in its interior positions gives the prefix. At even length suffix-pairs recognize the selected layers. For two pairs a reverse overlap would force the even-length middle word to alternate, with the entering step opposite its final step, contradicting selection; with one pair the missing one-step layer determines the next orientation. Once the prefix is known, the selected completion cannot be a predecessor of the other sibling: one step violates proper adjacency and two steps require a period-two word. Presence of that completion decodes the center. This uses at most five length-n labels and constant scans. For n=2 any source goes directly to the target if its last letter equals the target's first, otherwise in two shifts, and n=1 is complete in one step. Thus both boundary cases have coincident balls.

## originality

PASS

The exact incoming binary radius-two optimum for all ternary Kautz lengths and its orientation decoder are distinct from the inspected radius-one, full de Bruijn, domination and exact-distance results. There is a genuine boundary construction match at n=3 under restriction from full de Bruijn; this does not supply the Kautz all-length theorem. The unresolved line-digraph citation is not counted as either evidence against overlap or a positive prior match.

## value

PASS

The result settles an exact optimum and supplies an efficient decoder in a natural shift network and observation model. The decoder proves a real obstruction can be resolved at the lower bound; unlike simply selecting one sibling per pair, it deals with coinciding predecessor signatures, distinguishes parity, and covers all feasible lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
