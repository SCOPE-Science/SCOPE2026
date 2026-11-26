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

For a generic objective each edge has a unique maximizing endpoint. A different sign pattern changes at least one endpoint and strictly lowers the original objective applied to the sum, so distinct patterns cannot give the same vertex. Intrinsic projection preserves signs even for a disconnected graph; the uniform quantiles used for localization are those of the ambient i.i.d. Gaussian representative. Conditioning on the two core coordinates gives each private leaf agreement probability h=uv+(1-u)(1-v). Off the two matched corner squares h is bounded by 1 minus a positive constant, hence the discarded integral times n^(2k) vanishes. Within either corner, n times the distance variables converge under the integrand to independent unit exponentials, dominated by exp(-(1-delta) times the sum of distances). Opposite-color edges always agree; same-color edges give two uniform orderings, independently across the two induced subgraphs. This proves the sector weight, total limit and conditional law by division by the positive total; using any smaller corner size also establishes localization for all 0<delta<1/2. Adjacent swapping of the endpoints of a new edge witnesses a strict loss on each sector with both endpoints on one side, including the all-zero sector. The edgeless and complete bounds and equality cases follow; the path has order-class sizes 1,1,2,2 and kappa=41/9, and the triangle has kappa=10/3. CHECK.py and VERIFICATION.md were inspected, not executed; their recorded bounded rank enumerations do not establish the asymptotic. The analytic replay is RESULT.md §§Proof, steps 1–5, with the endpoint injectivity argument above.

## originality

PASS

The verified distinction is the fixed arbitrary private-leaf core with k>=3, its induced-subgraph partition coefficient, conditional sector weights and strict edge extremality. Graphical chamber probabilities and the one- and two-hub laws are antecedents. The strongest split-graph and bipartite analogues have shared rather than private leaves and do not give this statement.

## value

PASS

The coefficient distinguishes cores with the same number of hubs and pendant vertices (for example the path and triangle), the extremal law is strict under each edge addition, and the corner weights describe where collisions occur, none of which is supplied by merely counting zonotope vertices or orientations. The fixed core and prescribed metric make this a natural angular invariant rather than a selected finite case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
