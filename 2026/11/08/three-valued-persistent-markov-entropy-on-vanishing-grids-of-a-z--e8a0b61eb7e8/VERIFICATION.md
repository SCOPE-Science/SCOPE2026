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
The source proof determines all stationary weights analytically for every integer \(N\ge10\) and proves that the deterministic map has zero topological entropy and a physical period-two law. To replay exact finite checks, run `python verification/check.py` from the file root. This only uses Python's standard `fractions` and `math` modules.

The checker derives each row from exact overlap lengths, confirms row stochasticity, checks the closed class and reachability of the zero cell, and evaluates the stationary vector exactly for \(10\le N\le200\). It independently computes entropy values by direct Shannon evaluation. These finite computations corroborate the proof; they do not certify the universal quantifier. The procedure deliberately excludes PageRank teleportation and finite random sampling because they define different matrices.
