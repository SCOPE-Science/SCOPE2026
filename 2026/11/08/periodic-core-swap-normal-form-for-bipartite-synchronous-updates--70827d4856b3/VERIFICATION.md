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
# Reproducibility and verification

Run `python3 verify_finite_maps.py` and `python3 verify_majority.py` with Python 3 and no external dependencies. Compare standard output byte-for-byte against `verify_finite_maps.out` and `verify_majority.out`, respectively. The first script exhaustively compares direct iterates with the predicted odd/even fixed counts for all \(900\) map pairs of finite sets of sizes one through three, over twelve time indices. The second exhausts the specified \(189\) odd-degree bipartite graphs on two through six vertices, checks a ten-vertex odd-degree tree, and exhibits the tie-retaining majority failure on a four-vertex path.

The universal assertions are proved from the explicit conjugacy, not from these finite tests. This record includes no independent external certification. There is no claim that unindexed earlier literature has been ruled out.
