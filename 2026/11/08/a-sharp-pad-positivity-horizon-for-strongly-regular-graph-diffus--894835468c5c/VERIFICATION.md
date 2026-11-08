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

The standalone `check.py` was executed with Python's standard library. It constructed seven exact, unweighted strongly regular adjacency matrices and compared the direct rational Padé matrix \(T(h)\) with both algebraic off-diagonal formulas, along with exact stochastic row sums and positive diagonal entries. Output: `VERIFY_OK exact_offdiagonal_entries= 8172`.

The checked finite graphs were the Petersen graph, triangular graphs of orders \(n=5,6,7\), rook graphs with board dimensions \(3\) and \(4\), and the Shrikhande graph. Six distinct positive rational timesteps were checked per graph. The projectors and sign classification are established symbolically in `RESULT.md`; no finite matrix list proves the all-graphs/all-timesteps theorem.

No formal proof assistant and no independent mathematical audit are asserted. Reproduction uses `python3 check.py` with no third-party packages or network access.
