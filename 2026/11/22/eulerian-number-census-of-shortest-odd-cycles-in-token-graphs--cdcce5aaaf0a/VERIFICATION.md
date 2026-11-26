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

For any closed odd token walk the mod-two chain of projected base edges has zero boundary and odd weight. It contains an odd simple cycle, so its weight and the original walk length are both at least g. Equality forces each edge of that unique shortest base cycle to be used exactly once, all outside occupancies fixed, and occupancy conservation forces the directed moves to follow a common cyclic orientation. With that orientation chosen, a vertex starts occupied exactly when its outgoing edge is earlier than its incoming edge. This criterion is sufficient as well as necessary: a vertex toggles only on its two incident moves and is ready at both. No proper nonempty subset of the base cycle has zero mod-two boundary, so each legal g-step tour is a simple token cycle. Re-rooting edge-time lists at their maximum gives g times the indicated Eulerian number; dividing by g forgets the token cycle's start, without an extra factor of two because the movement direction was fixed. The feasible h interval [max(1,k−(n−g)),min(k,g−1)] is nonempty for every stated k. Outside choices give the binomial coefficient, and bipartite base graphs give a two-coloring by token parity. At g=3 Pascal's rule gives the known triangle count, and the g=7 Eulerian row agrees with the example. Inspected VERIFY.py and the recorded finite check (39 base graphs, 126 token counts); did not rerun it. The parity and edge-order arguments, not enumeration, establish the general theorem.

## originality

PASS

The triangle lift/count and bipartiteness inheritance are prior work. The distinct content is the all-shortest-odd-length census beyond triangles, with unique supporting shortest base cycle and Eulerian multiplicity. The strongest ring specialization overlap counts the members of a particular decomposition rather than all cycles. The assessed novelty is bounded by the sources inspected.

## value

PASS

This counts a standard graph invariant for arbitrary graphs of prescribed odd girth, all token numbers, and all base components, rather than just determining whether a lifted odd obstruction exists. The unique-parent structure explains precisely why shortest odd token cycles cannot combine moves on different base cycles and makes the count depend only on n, k, g and the base shortest-cycle census. It generalizes the practically useful triangle calculation with a nontrivial Eulerian factor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
