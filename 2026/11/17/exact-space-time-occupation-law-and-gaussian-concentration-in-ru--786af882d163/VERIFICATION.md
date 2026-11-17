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

Three executable verification programs are provided under `verification/` and require only Python 3, SymPy, NetworkX and NumPy. The symbolic program rebuilds all 512 three-history transitions, identifies 19 cyclic vertices, and proves the exact factored weighted characteristic determinant. The independent simulator enumerates all indexed original binary states for circumferences 3 through 17 and compares weighted returns at weight 2, the fixed-state subtraction, and orbit counts. The spectral program gives an exact rational positive-vector Perron bound, root sign and root-count checks, and directed cycles of coprime lengths.

Recorded `.out` files correspond to successful execution of the accompanying source. They are reproducibility evidence for the finite symbolic certificate and tested lengths, not an assertion that finite simulation alone proves the infinite-family formula. The infinite-length result is derived from the exact transfer graph and Perron–Frobenius theory. Independent outside assessment has not been performed.
