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

## Reproducibility
Run `python check.py` to enumerate and weight all Birkhoff-skeleton edges in order six, compute all vertex distances by Dijkstra's algorithm, and check the claimed formula for every permutation moving at most five elements and for every triple transposition. Run `python check.py 7` for the corresponding order-seven test. Both modes separately count the ordered 3-cycle/6-cycle decompositions of a canonical triple transposition and assert 16 in each order.

The finite tests use floating-point square roots and absolute tolerance \(10^{-9}\). Exact all-dimensional validity comes instead from the support lemma, parity and concavity bounds in `RESULT.md`. These tests do not provide independent audit or historical-priority certification.
