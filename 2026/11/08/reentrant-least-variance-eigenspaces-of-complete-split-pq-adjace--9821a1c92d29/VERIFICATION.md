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

Run `python3 artifacts/verify.py` with the Python standard library. The program reconstructs every directed edge-or-loop vertex and its two one-hot coordinate blocks, forms the exact integer covariance numerator \(N^2C\), and checks a full eigenvector basis consisting of within-class contrasts, class contrasts, and two zero modes. It verifies the phase sign identity for each profile. Expected output: `PQ_SPLIT_COVARIANCE_CHECKS_PASSED 85 parameter_cases 209596 matrix_entries`.

The explicit tested profiles range over clique sizes \(2\) through \(9\) and selected independent sizes at and away from the predicted boundaries. Exact integer comparisons avoid floating-point ambiguity. The infinite-range phase theorem is established by the quadratic proof, not by these finite examples. A numerical eigensolver was also used separately for several small and medium examples; that optional exploratory calculation is not needed to reproduce the theorem.

The result uses only the standard Euclidean coordinate representation and a uniform distribution over distinct vertices. Independent mathematical audit has not been performed.
