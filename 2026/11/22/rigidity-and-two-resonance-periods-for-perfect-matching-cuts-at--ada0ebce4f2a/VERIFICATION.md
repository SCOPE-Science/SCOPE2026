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

# Reproducibility

The supplied `certify_transfer.py` generates the exact local \(2k+2\)-bit windows for every \(k\in\{4,5,6,7\}\), constructs the directed overlap graph, finds all cyclic strongly connected components, tests their internal indegrees and outdegrees, and asserts that their lengths are exactly the theorem's periods. The transition graph enumerates \(2^{2k+2}\) candidate bit windows, including all possibilities, not random samples.

`verify_direct.py` independently enumerates every cyclic independent transition word with the required even parity, reconstructs the colors of each graph vertex, and checks the original perfect-matching-cut condition for every vertex, for every \(2k+1\le n\le24\). Its implementation does not use the finite-state graph. The exact outputs are embedded in `transfer_output.txt` and `direct_output.txt`.

Use `python3 certify_transfer.py` and `python3 verify_direct.py` with Python 3; no third-party packages or network access are needed. The complete local-state classification proves the infinite case. The independent direct tests only validate the reduction in finitely many instances. Neither program nor the mathematical argument establishes an analogous classification for \(k\ge8\), and no independent scholarly audit has been performed.
