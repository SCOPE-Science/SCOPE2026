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

A subtournament is acyclic exactly when it has no directed triangle. Since all arcs among U=T-h point forward, a triangle through h is cyclic exactly for an outneighbor o followed by an inneighbor i. This gives the full simplex on U glued to the h-cone on the independence complex of the corresponding forbidden-pair graph. For nonempty O use p=max O. Its neighborhood is contained in that of any other o in O, so adding p to an independent face containing o but not p is legal. In descending size every competing proper coface has already been removed with a larger pair, proving these are elementary collapses. Once all such o are removed, an isolated vertex gives a cone, an edgeless graph a simplex, and otherwise the remaining star gives a center point disjoint from the simplex of leaves. The last case occurs exactly when both O and I are nonempty and all O precede I. Each link pair lifts to a free pair containing h because the base contributes no coface of it. In the single-edge case collapse h and then the base; in the two-edge case collapse the base relative to the edge of the two surviving endpoints, giving the literal three-edge boundary. The all-in and all-out patterns are in the collapsible case, including for n=3. The n-2 count is the number of proper nonempty initial segments of the fixed order. The archived 4,092-case run (196 circle cases) is recorded corroboration, not rerun or needed for the proof.

## originality

PASS

The chain-graph fold, cone and simplex collapses are standard, and some homotopy and fundamental-group aspects have prior coverage. The inspected results do not supply the uniform feedback-one criterion with actual elementary free-face collapses to the specified simplicial subcomplexes. Credit that statement and its explicit application of the ingredients, not a new fold or a new general theorem about tournament fundamental groups.

## value

PASS

The transitive-deletion-one case is a natural first case beyond a simplex. The result gives an explicit reduction and an exact orientation criterion, upgrading homotopy information to a verifiable elementary collapse of the original complex. This identifies the obstruction in the smallest nontrivial deletion class and provides a baseline for larger feedback sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
