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

# Reproduction and scope

The standalone `verify.py` uses Python 3 with NumPy and SciPy. Execute `python3 verify.py` from the directory containing `RESULT.md`. It independently constructs all induced complete-bipartite rank halfspaces, solves ambient ball linear programs on twelve small graphs, checks the unique predicted center and all biclique slacks, compares full two-variable minima against the theorem's cutoff formula for several families, and tests the special sharp ten-vertex threshold.

Observed result: `PASS: 3133 grouped mathematical checks; complete facet LP for 12 cases`.

The infinite parameter ranges are justified by the analytic minimax and derivative arguments in `RESULT.md`, not by these finite checks. No external independent audit has been performed.
