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

# Reproducibility and limits

Execute `python verify.py` using Python 3.10 or later; no packages are required. The script builds the incidence-algebra basis, multiplication, every coefficient of the skew derivation equation, and the linear map from inner generators to skew derivations. Gaussian elimination modulo prime fields gives the dimensions without using the proof's cochain classification. Separately, cochain coboundary matrices are built from fixed vertices and compatible edges; the predicted classification is checked against the cochain ranks.

Observed output:

```
COCHAIN_CASES 900
DIRECT_SKEW_LEIBNIZ_CASES 144
PROBABILITY_MOMENT_CASES 51
VERIFY_OK
```

The direct algebra checks use \(m\in\{3,4,5\}\), prime fields of sizes \(2,3,5\), every rotation and reflection, and different edge scalings. Additional cochain checks reach \(\(m=12\)\) and moments are checked up to \(\(m=19\)\). No result about all finite fields or arbitrarily large crowns follows solely from these finite computations. The proof uses the literature-established skew-cohomology isomorphism and explicit modular-neighbor calculations for every size; the verifier is independent finite evidence.

The automorphism-group cardinality is obtained mathematically from the unit group and fractional multiplicative automorphisms rather than by exhaustive enumeration of all algebra automorphisms.
