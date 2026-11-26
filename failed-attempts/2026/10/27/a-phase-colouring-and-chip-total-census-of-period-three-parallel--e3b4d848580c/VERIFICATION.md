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

Three-step net change is the graph Laplacian of the per-vertex firing counts. Its kernel is constant on the connected graph; counts 0 and 3 give fixed states, so least period three has count 1 or 2. At count 1, assigning each vertex its unique firing time makes its time-t chips equal to the initial count plus earlier neighbor firings minus its degree if it has already fired. Enforcing the three threshold inequalities gives exactly [d,d+h_2−1], [d−h_0,d−1], or [h_2,d−h_0−1] according to phase. Choices are independent with phases fixed; actual updates follow inductively and the net firing count gives return. A coordinate at least 2d forces the same threshold and a firing at each preceding time around the orbit, which is impossible here. On the resulting box the chip complement flips all firing indicators and commutes with the map, giving the reflected total and bijecting the one- and two-fire families. No fixed state can have one or two firings over three time steps. For complete bipartite graphs each nonempty shore support must contain all phases by repeatedly taking the predecessor phase across shores. With a thin shore of size three there are six choices for its phase assignment and a right-shore witness for each phase, giving b(b−1)(b−2)3^{b−3} times six and the complement factor two. Independent direct enumeration agrees with the full chip-total histograms on K_{3,3} and K_{3,4}.

## originality

FAIL

The decisive earlier coverage is Prisner (1994), Lemma 6.7 and the completeness statement immediately after its proof, not merely a prior existence theorem. Its vertexwise phase-partition construction covers all periodic states of activity 1/p in a broader Eulerian multidigraph setting. Specializing to p=3 and replacing each undirected edge by the two reciprocal arcs gives the complete one-fire family. The three lower endpoints and widths are the local threshold inequalities for those assigned phases, and counting the independent initial choices by chip total is the direct generating-product rule. The other family is the standard chip complement. The thin-shore formula is the immediate witness count in this same specialization. There is an exact later catalogue overlap, but the originality failure rests on the earlier complete constructive coverage, not on catalogue path order or inability to access a source.

## value

FAIL

Conserved chip totals and exact state counts are natural invariants, and the two thin-shore histograms are useful checks. But the frozen contribution is only to take the product of vertexwise interval generating factors in the earlier complete phase construction, reflect them, and count witnesses in its simplest complete-bipartite specialization. This does not establish a distinct structural or exact enumerative result beyond a mechanically obtainable corollary. Stronger energy-support results in a different record are not part of this frozen submission.

The dated certificate retains the supplied scientific assessment, sources and limitations.
