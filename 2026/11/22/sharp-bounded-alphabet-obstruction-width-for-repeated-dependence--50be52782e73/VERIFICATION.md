---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Because the atoms are downward closed, the lax cover can be disjointified. A matching assigning each ordered pair to one of the r slots at its row or the one slot at its column exactly realizes the partition (the repeated row atoms provide separate slots). For any collection of pairs, the union of its slots has size r times its row-support size plus its column-support size. Hall is therefore equivalent to the inequalities on all support rectangles; the team is finite, so finite supports suffice even if the ambient alphabets are infinite. For a minimal false team, no edge can be outside a violating rectangle, and reducing to the actual supports preserves violation. Thus with a rows and b columns it has ra+b+1 edges, since any deletion must restore the full-support inequality. A row with at most r edges could be deleted and then restored using that row’s own slots, so every row has at least r+1 edges. Hence a≤b+1≤q+1 and the stated sharp upper bound follows; q≤r trivially allows all edges to use row slots. At equality the team has a=q+1, b=q and all degrees r+1. For a proper set of columns S, taking all rows with N(x) contained in S shows the necessity of the multiset condition. Conversely, a row not contained in S contributes at most r edges to the rectangle, so the condition suffices for every proper column set; with all columns the inequality also holds for every proper row set. The full rectangle has excess one and deleting any edge restores it. For existence the q cyclic windows of length r+1 plus a duplicate of the zero window satisfy the condition: when any window fits in a proper S, the maximal cyclic runs in S give at most |S|−r fitting starts before the duplication. When q=r+1 no proper S contains a whole window, so even all neighborhoods coinciding is valid. For r=2 and q=4 the five row neighborhoods 012,123,230,301,012 explicitly give 15 pairs, not a 4×4 team. A minimal false subteam exists in every finite false team. Replay: RESULT.md lines 22–46; the bundled finite checker was inspected, not executed.

## originality

PASS

The frozen finding expressly treats r=1 as an existing specialization; the earlier finite unequal-alphabet spectrum covers its width. The supported contribution of the general theorem is the sharp width with only the column alphabet bounded for all multiplicities, its uniform attaining construction, and the equality characterization. Neither Hall’s criterion nor the fixed 4×4 census is credited as new.

## value

PASS

For a natural disjunction of repeated functional dependencies, the finite column alphabet is an intrinsic restriction that turns non-uniform obstruction size into an exact finite witness guarantee. The result locates the entire vacuous regime, gives witnessed sharp linear growth with q at each multiplicity, and characterizes the extremal support systems rather than only restating a matching algorithm. The contrast with the smaller 4×4 maximum shows concretely why bounding just one alphabet is a different regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
