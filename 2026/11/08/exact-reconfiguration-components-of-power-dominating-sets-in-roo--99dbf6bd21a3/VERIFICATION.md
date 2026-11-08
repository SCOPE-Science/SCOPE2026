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

Run `python3 verify_rook.py` with Python 3.8+ and no third-party packages. The script constructs each rook graph directly, simulates the closed-neighborhood and unique-neighbor propagation rule, and builds bounded token-addition/removal graphs on all feasible subsets by explicit one-bit adjacency. It verifies every nonempty subset and every budget from the minimum through \(n\) for eight boards.

Expected results include component vectors \((75,1,16,1)\) for the \(3\times5\) board at budgets \(2,3,4,5\), and \((108,1,1,19,1)\) for the \(3\times6\) board at budgets \(2,3,4,5,6\). All comparisons must return `PASS` without exception.

This is finite independent algorithmic corroboration of the structural classification and the component formulas. Proof of the unrestricted claim is mathematical, in RESULT.md; no external or independent audit has been performed.
