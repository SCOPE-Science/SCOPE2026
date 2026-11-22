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

# Reproducibility and verification

The entire universal claim is proved in `RESULT.md`, from the finite quadratic chirp formula, a factorization valid off the distinguished circle, exact trigonometric modulus-one conditions, and a complete unit-circle ratio-graph clique classification. No numerical sampling is used to infer absence of untested zeros or a global classification.

Execute `python3 checker.py` with Python 3 standard library. The checked program performs all arithmetic with exact rational real/imaginary pairs. It verifies 48 distinct rational unit-circle points for the continuous family; the fixed discrete Fourier configuration; the 16-vertex fourth-root-of-unity ratio graph; all 12 orthogonal four-subsets on that grid, classifying eight as continuous-type and four as isolated-type; and all 56 undirected orthogonality edges on that grid. Each exact test completed successfully before this review.

The finite diagnostic grid cannot prove a statement for arbitrary continuous phases; the analytic factorization and graph casework in the result supply the proof. The general order-four complex Hadamard classification is a known comparison theorem and is not claimed as an independent result here. No separate human or independent audit was performed.
