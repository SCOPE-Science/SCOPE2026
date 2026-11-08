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

The reproducible verifier is `verify.py` (Python 3 standard library). Running `python verify.py` finished successfully with `VERIFY_OK`. It directly enumerates ordered pairs of elements of the algebra and multiplies them over the prime fields of sizes two and three on small paths, checking every orientation; it also checks selected small parallel-arrow and cyclic examples. Independent enumerations of the weighted-subgraph expansion verify the polynomial recurrence and the strict two path extrema through six and five vertices, respectively. A three-edge star checks uniqueness of the bipartite maximizing orientations. Finally, simple real-number computations check the two Perron roots for three field sizes. These are finite consistency checks: the universal statements require the exact algebraic counting and spectral arguments in `RESULT.md`. Independent audit has not been performed.
