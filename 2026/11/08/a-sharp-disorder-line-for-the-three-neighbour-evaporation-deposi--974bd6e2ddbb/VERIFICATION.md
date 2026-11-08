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

Run `python verify_disorder_line.py` in an environment with NumPy and SymPy. The test executes symbolic characteristic-polynomial/discriminant identities and finite-ring comparisons between independent configuration enumeration and transfer-matrix traces, including occupation pair sums. It also checks parameter samples on each side of the root curve, and a rational example with exact complex roots. Recorded output: `PASS 310 symbolic, transfer-matrix, finite-ring and spectral checks`.

The transfer-matrix/renewal proof, not the finite computations, establishes the infinite-volume limit and the long-distance asymptotic. The tests do not check all real parameter values, prove novelty, or constitute independent review. The full analytical stationary-measure identity is credited to the cited primary source, and is not proved anew. Independent finite-state transition-kernel spot checks verify its stationary balance for representative rings of size three through six.
