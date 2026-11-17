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

# Reproduction of exact cellular calculations
Run `python3 verify_chessboard.py`. The standalone program uses only Python standard library and reconstructs every legal face, each matched and critical face, the complete directed Hasse cover graph, and the exact signed Morse incidence matrices. It performs a topological sort, checks the chain-complex relation and runs integer-only unit-pivot elimination. The output is embedded as `verification_output.txt`.

The verified results are: 8,835 / 15,933 / 18,873 faces including the empty face; 40,544 / 76,958 / 92,848 covers; 4,406 / 7,901 / 9,312 matched pairs; unit cancellation ranks 3; 1+35; 2+93. The final complexes retain one zero-cell plus 15, 57 or 57 five-cells.

Acyclicity and incidence identities are checked on complete finite complexes. No claim of independent mathematical audit, equivariant naturality, or broader parameter classification is made.
