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

# Reproduction and limits

Run `python3 heawood_edge_bases_verify.py` and `python3 heawood_edge_bases_verify_alt.py` in any Python 3 interpreter with the standard library. The outputs must exactly match `heawood_edge_bases_verify.out` and `heawood_edge_bases_verify_alt.out` respectively. Both were run successfully. The first certifies 21 incidence edges, graph-distance edge vectors, all candidate bases of sizes zero through five, and the jump and slide graph parameters. The second uses distinct distance formulas, directly constructs all geometric candidates, checks the same minimum and complete five-subset census, and independently identifies all 21 eight-cycle slide components with the graph's eight-cycles.

The source of truth is the explicit 14-vertex incidence graph; no file outside the package is needed. The certificate is exhaustive for this graph, not an extrapolation to higher order planes. No external independent audit or certification was performed.
