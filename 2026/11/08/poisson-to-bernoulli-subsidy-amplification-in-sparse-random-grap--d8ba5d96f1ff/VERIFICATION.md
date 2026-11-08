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

Run `python3 verify_graph_subsidy.py` with Python 3.9 or newer. The verifier uses only the standard library, exhaustively checks every graph with at most four vertices, confirms six five-vertex archetypes, and evaluates exact independent-edge expectations at two finite sample sizes. Expected final output: `PASS: 81 exact graph-orientation subsidy tests; two expectation checks`.

These checks corroborate finite instances only. The general deterministic equality and infinite Poisson, concentration, distribution and expectation limits are established in `RESULT.md`. To verify the proof by hand, first check the indegree-zero tree lower bound and subsidy propagation to isolates, then the cycle-and-tree orientation construction; independently reproduce the factorial moments for isolated edges, all three ranges of the tree-component bound, and the isolated-vertex covariance calculation. No independent scientific validation was performed.
