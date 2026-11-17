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

# Reproducibility

Run `python3 verify_prism_quotient.py` alongside `certificate.json`. The checker requires only the Python 3 standard library and reconstructs the graph, symmetry action, all matchings and barycentric flags rather than trusting precomputed face lists.

The observed nonempty matching-face vector is \((15,75,145,95,11)\), the complete flag vector is \((341,2680,5940,4920,1320)\), and the genuine orbit-cell vector is \((35,188,357,276,72)\). Burnside's lemma is independently evaluated for every dimension; all boundary compositions are checked exactly. The certificate's unit pivots have counts \((34,154,203,72)\) in differential dimensions one through four, leaving two free cells with zero differential. The fundamental-group certificate gives a 34-edge spanning tree and 154 generator-killing witnesses in four rounds with lengths \((97,36,17,4)\). The terminal success marker in the accompanying actual run is `INTEGRAL_PRISM_QUOTIENT_VERIFY_OK`.

Only the finite algebraic computations are checked by the script. The mathematical interpretation additionally uses the no-inversions orbit CW lemma, elementary integral chain contraction, the standard presentation of the fundamental group of a connected two-skeleton, and the Hurewicz and homological Whitehead theorems. No claim of formal machine-checked topology or independent validation is made.
