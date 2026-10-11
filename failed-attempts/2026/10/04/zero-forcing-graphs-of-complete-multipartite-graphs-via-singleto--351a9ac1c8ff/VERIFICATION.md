---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

For a noncomplete complete multipartite graph, a successful zero forcing process cannot start with three or more white vertices: any first force leaves at least two indistinguishable white vertices in one part and the process stalls. With exactly two whites, forcing succeeds precisely when they lie in distinct parts and are not both singleton parts. Thus minimum sets are exactly complements of those admissible pairs. Merging singleton parts makes admissible pairs exactly the edges of the compressed multipartite graph \(H\); two complementary minimum sets differ by one token exactly when their omitted edges share one endpoint, so the reconfiguration graph is \(L(H)\). The order and diameter statements follow. Fresh exhaustive checks on profiles \((2,2),(3,1,1),(2,3,1),(1,1,1,1),(1,3)\) reproduced the minimum-set counts and diameters.

## originality

FAIL

A published SCOPE/Resultary theorem already classifies every \(k\)-forcing set of every connected complete multipartite graph. Its \(k=1\) specialization gives exactly the minimum ordinary zero forcing sets for arbitrary part profiles, including singleton parts. Once those minimum sets are represented by their omitted admissible pairs, the submitted reconfiguration graph is mechanically the line graph of the graph whose edges are those pairs, because token-jumping adjacency is exactly one shared omitted endpoint. Thus the substantive classification is covered and the remaining line-graph reformulation is a routine consequence of the definition. Earlier external work also already defines the reconfiguration graph and treats complete/star boundaries.

## value

FAIL

After the published all-\(k\) classification supplies every minimum zero forcing set, identifying the token-jumping graph with a line graph is a one-step change-of-encoding: vertices are omitted edges and adjacency means shared endpoint. The order and diameter follow from elementary line-graph facts. This is a useful corollary but not a sufficiently independent mathematical contribution under the common value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
