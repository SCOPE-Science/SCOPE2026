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

The reproducible standalone checker is `check.py`; execute with `python3 check.py`. It requires only the Python standard library. The independently stored expected output is `check_output.txt`.

The enumerator traverses every partition of old points, then every partition of those blocks, and turns each nested partition into its canonical unordered hierarchy signature. Therefore its assertion that the first pair with identical levelwise ball-size multisets appears at five old points is exhaustive for heights three and old sizes at most five. The checker separately assigns each new point every consistent singleton distance profile and every internal pair-distance value, tests all ultrametric triples, and recovers exactly the same counts as the iterated exponential-generating functions through new-arity four. It also checks finite-height inversion determinants for heights two through seven; the all-height proof is in `RESULT.md`, not inferred from these finite checks.

No claims about higher-point exhaustive census, verification by an independent expert, or complete historical priority follow from these computations.
