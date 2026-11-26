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

Verified the fixed-tree proof in RESULT.md lines 40–55. A queried edge witnesses its own empty singleton trace, and in a tree with ≥2 edges it has a neighbor. For a support of two edges incident at u, the two own-edge witnesses realize the singleton traces, an extra edge at u is required for the full trace, and the empty trace requires either a second edge in an unchosen branch or a third edge in any branch. When no branch extends three edges, precisely those pairs containing every depth-two branch fail the empty-trace condition, giving B_u. For a disjoint pair, the middle edge of their unique three-edge connecting path is the only possible joint witness, and another edge is needed at an endpoint of each outer edge for each singleton, giving the two degree-sum tests. Any all-support witness splits the support among its endpoints. For a mixed support of size ≥3, choosing one edge from each side gives a disjoint pair whose only common neighbor is the all-support witness, so the pair trace is missing. The remaining triples are stars: the omitted support edge gives each doubleton, each singleton requires extension on its chosen branch, and the same branch test gives the empty trace. Four-edge stars have no two-element trace, excluding them and all larger supports by heredity. Eight distinct witnesses are necessary for a shattered triple; the four length-two arms supply them on nine vertices and give four shattered triples. The attached Prüfer verifier was inspected, not executed; the separately reported unlabeled census is corroboration only.

## originality

PASS

Pass for the explicit branch/degree formulas enumerating shattered supports of each tree line graph and their sharp nine-vertex threshold. The same-day block-graph theorem already implies the degree-three upper bound as a statement, irrespective of unresolved relative priority. The upper bound alone is not credited as distinct. The relevant broader results count traces on a prescribed support, not how many supports in a fixed tree attain all traces.

## value

PASS

The exact per-tree census gives structural information not furnished by a sharp class maximum: it identifies separate depth-two and depth-three branch effects and counts supports for every tree without enumerating all witnesses against all supports. The nine-vertex witness and counting lower bound fix a meaningful first occurrence of the top-degree term. The result is restricted to open line-graph neighborhoods with internal witnesses allowed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
