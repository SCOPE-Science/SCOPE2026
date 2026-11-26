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

For a graph of maximum degree three the rule is the even-count rule. Over F_2 the symmetric matrix M=I+A has z^TMz=sum z_i for all z, so the all-ones vector is orthogonal to ker M and hence belongs to im M. A universal vertex by itself is an equilibrium; absence of a universal vertex through order five gives maximum degree at most three. Disconnected graphs split componentwise, and the empty graph has the vacuous equilibrium. For the eight-edge graph, the internal path equations force the two hub actions equal. The two common degree-two neighbors are then active; active hubs see at least three, while inactive hubs would require both internal path vertices active in contradiction to the path equations. The nine-edge graph is the 3-sun. Zero active hubs, or one or two active hubs, forces at least one inactive hub with two active neighbors; three active hubs gives degree-four active counts incompatible with activity. In a fresh exhaustive run (`python3 /workspace/reproductions/1.py`), for every labeled graph through six vertices the set of putative active vertices was compared to the defining set of strict best responses. The census (connected, failing) was (1,0),(1,0),(4,0),(38,0),(728,0),(26704,300). The two display graphs' full relabeling orbits were disjoint and their union was exactly the failing set; their sizes and minimum masks were (180,957) and (120,1915). The supplied checker was inspected, not run. Its Python 3.8 compatibility note is inaccurate because int.bit_count requires Python 3.10+, and the nonzero-equilibrium remark applies only to nonempty graphs. Neither affects the theorem.

## originality

FAIL

A distinct indexed Resultary record explicitly states the same rule, sharp cutoff, two edge lists and orbit counts. The printed literature also already contains the nine-edge 3-sun witness, though the inspected papers do not give the full census. Exact coverage by the distinct catalog record is established; historical timestamp authentication and who reached the result first are separate questions.

## value

FAIL

The sharp minimum graph order and exact first obstruction set are naturally useful beyond a single gadget, but the separate catalog record already supplies both and the same census. Rechecking that census adds no new graph boundary, structure or independent exact invariant to the stated finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
