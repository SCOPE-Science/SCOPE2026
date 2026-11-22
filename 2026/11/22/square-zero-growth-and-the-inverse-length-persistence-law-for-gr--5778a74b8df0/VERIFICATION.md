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

# Verification record

The mathematical derivation uses unique graph-inverse-semigroup normal forms, explicit prefix-cancellation multiplication, exact adjacency-path generating functions, and a Perron-Frobenius pole expansion. The script `CHECK.py` independently enumerates normal forms and computes their actual squares and subsequent powers, while deriving expected coefficients by matrix multiplication. It reports all eight graph checks passing through length six or eight.

The finite tests include multiple edges, a period-two graph, an acyclic graph, a graph with isolated vertices, and primitive graphs. They are finite corroboration only; the full theorem follows from the proof in `RESULT.md`. No external proof certificate and no independent scientific audit are claimed.
