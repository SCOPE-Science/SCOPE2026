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
# Reproducibility and limits

Run `python3 gp_tensor_verify.py` with Python 3.8+; no nonstandard libraries are required. The program constructs the graph by its coordinate adjacency rule, obtains all-pairs distances by Floyd–Warshall, enumerates every vertex subset for the six cases \((a,r)=(3,3),(3,4),(4,3),(3,5),(5,3),(4,4)\), and tests all selected triples against geodesic equality. It separately computes all coefficients by the structural binomial formula and compares them. It also checks the exact four-part unimodality decision for each integer \(r\in[3,1000]\), plus a concrete coefficient discrepancy against the displayed 2024 formula at \(a=r=3\).

Observed stdout from the source program before packaging:

`VERIFY_OK direct_graph_instances=6 tested_vertex_subsets=139776 a4_unimodality_r=3..1000 source_discrepancy_a=r=3_48_vs_66=PASS`

The computations are exhaustive only for the six listed finite graphs, not over unbounded \(a,r\). The unrestricted formulas and sharp four-part interval rely on the proof in `RESULT.md`. No independent audit is asserted.
