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
Run `python3 check_quad_graph.py` with Python 3.8 or later, without installing dependencies. The program constructs graph-indicator windows, computes all Walsh ambiguity coefficients exactly, checks the complete multiplicities for all dimensions \(1\le m\le6\) and all possible polar ranks, and independently diagonalizes the full shifted-projector Gram matrix for three cases. Expected final lines:

```
BINARY_QUADRATIC_GRAPH_AMBIGUITY_CHECKS_OK
GRAM_EXACT_OK m 2 r 1 eigs [(0, 35), (32, 28), (128, 1)]
GRAM_EXACT_OK m 3 r 1 eigs [(0, 198), (256, 56), (1024, 2)]
GRAM_EXACT_OK m 4 r 2 eigs [(0, 707), (512, 256), (2048, 60), (8192, 1)]
EXACT_PROJECTOR_GRAM_CHECKS_OK
```

The checker uses exact integer arithmetic only. The proof in `RESULT.md`, specifically the complete hyperplane Walsh calculation and Weyl orthogonality, covers infinitely many dimensions and polar ranks; the finite checker does not itself establish an infinite statement. Generic weighting is proved by nonvanishing of finitely many explicit real polynomials, not by a numerical sampling experiment. Normalization and physical interpretation limits are stated in the result. No independent validation has been performed.
