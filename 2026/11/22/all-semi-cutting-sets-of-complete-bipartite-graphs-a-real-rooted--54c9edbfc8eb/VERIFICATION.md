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

## Reproducible finite checks
Use Python 3 standard library and run `python3 verify_semicut.py`. It constructs each labelled biclique and its fixed terminal set, computes all original terminal-pair distances via breadth-first search, deletes each possible edge subset, and independently recomputes terminal distances to count every semi-cutting solution by cardinality. It compares these direct counts with the algebraic formula for 92 graph-and-terminal configurations with at most ten edges. It additionally tests the minimum cardinality, count, and universal lower bound for 92 larger configurations.

Observed output:
```
INDEPENDENT_TERMINAL_PAIR_BFS_AND_POLYNOMIAL_PASS cases= 92
EXTREMAL_POLYNOMIAL_AND_BOUND_PASS cases= 92
VERIFY_OK
```
The unrestricted conclusion is established by the four-block shortest-path proof, not by sampling. Independent mathematical audit has not been performed.
