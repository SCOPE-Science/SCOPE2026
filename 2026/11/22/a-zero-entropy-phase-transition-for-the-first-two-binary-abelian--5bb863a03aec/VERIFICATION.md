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

The proof is a finite graph argument, not a conjecture inferred from data. All admissible five-letter states and six-letter transitions are written in `RESULT.md`, where each edge can be checked by examining only the two candidate successor bits. The graph's two recurrent cycles and its finite entry/exit paths give the all-length classification.

Run `python3 graph_checker.py` to rebuild the state graph from the definition, verify its complete adjacency table, and check the recurrence through length 500. Run `python3 bruteforce_checker.py` to enumerate words independently through length 19, and to confirm the known full-Abelian-cube length-nine/tenth-length cutoff separately.

Both programs were run successfully for this package. Computations check the definitions and short cases; the mathematical proof for arbitrary length is the explicit directed-graph decomposition. No independent mathematical audit has been performed.
