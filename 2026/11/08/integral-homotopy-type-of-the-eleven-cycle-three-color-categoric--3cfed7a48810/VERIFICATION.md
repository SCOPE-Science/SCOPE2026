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

# Reproducibility and boundaries

Execute `python3 verify_c11k3.py` in the directory containing `morse_matrices.json`. Python 3.10+ is sufficient and no external dependencies are needed. A complete successful run outputs one JSON line beginning with the `certificates` field and containing the result marker `C11_K3_INDEPENDENCE_INTEGRAL_WEDGE_VERIFIED`.

The implementation enumerates all 732,802 faces (including the empty face), independently checks their cardinality distribution using eight possible color subsets at each of eleven cyclic sites, constructs two distinct 366,383-pair acyclic matchings, verifies 5,573,766 directed Hasse incidences per matching, regenerates the complete exact signed \(18\times16\) integral boundary in each critical basis, and checks fifteen unit pivots by explicit unimodular operations with zero residual matrix. The two outputs agree on reduced integral homology ranks three in degree six and one in degree seven. The absence of other critical positive-dimensional cells and the dimension gap in the Morse CW model establish the complete homotopy type after integral cell cancellation.

The embedded `verification_output.txt` is a record, not a substitute for executing the checker and inspecting `morse_matrices.json`. There is no assertion about larger cycle lengths, equivariance, or independent external validation.
