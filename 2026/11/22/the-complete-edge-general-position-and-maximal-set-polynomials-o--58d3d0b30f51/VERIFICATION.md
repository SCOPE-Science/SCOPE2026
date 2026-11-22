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

Both complete finite verifiers were run directly from their included source code against the labelled four-cube \(Q_4\). Each independently generated 576 shortest-path triples, counted 610955 legal sets and 4686 inclusion-maximal sets, and agreed on all 17 legal-size coefficients and every facet coefficient. The Python code also verified all six maximum sets are precisely the coordinate-class pair unions. Exact command/output transcript without private data is in `verification_output.txt`; re-run from scratch with `g++ -O2 -std=c++17 verify_q4.cpp -o verify_q4 && ./verify_q4` and `python3 verify_q4_independent.py`. The proof is finite and exhaustive, not a claim of an independent external audit, historical priority certification, or a higher-dimensional formula.
