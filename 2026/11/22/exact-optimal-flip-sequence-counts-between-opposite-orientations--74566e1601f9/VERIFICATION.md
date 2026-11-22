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

# Verification

The extracted standalone `check_geodesics.py` uses only Python's standard library. It compares the exact series recurrence against a monotone edge-flip dynamic program for \(1\le n\le8\); then runs unrestricted BFS in the undirected state graph (allowing all permitted edge reversals) for \(1\le n\le7\), computing distances and numbers of shortest paths from the uniform starting orientation. It separately enumerates the valid orientation and flip-edge counts through \(n=8\). The exact output of these runs is in `check_output.txt`.

To reproduce: `python3 check_geodesics.py`.

The Python checks are finite and do not establish the asymptotic or any conclusion for all positive integers. Those claims rely on the busy-period bijection, formal-series coefficient argument and explicit uniform convolution estimate in RESULT.md. The proof is self-reviewed; independent validation has not been performed.
