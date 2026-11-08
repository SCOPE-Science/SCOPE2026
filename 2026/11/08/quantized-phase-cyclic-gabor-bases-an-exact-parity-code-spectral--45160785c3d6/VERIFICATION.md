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

The exact Fourier-fiber calculation uses the sum of all \(p\)-th roots of unity and cyclic half-period pairing. The arithmetic law uses the determinant-two integer map from pairwise phase ratios to twisted adjacent differences. The parity enumerator counts all exact feasible alphabet words; no numerical searches are used to infer an all-size statement.

Run `python CHECK.py` after installing the dependency in `REQUIREMENTS.txt`. The checker exhaustively enumerates all phase-ratio vectors for \(p=2,3,4,5\), \(q=2,\ldots,8\), verifies exact probability counts at seven thresholds, checks the sharp optimum and optimal-ratio counts, and additionally compares independent full-matrix eigenvalue computations with the fiber formula for multiple randomly chosen phase windows. The actual output was `QUANTIZED_GABOR_TESTS_PASSED 1630`.

No external independent mathematical audit has been performed. Finite computations are corroborative only; the all-integer theorem follows from the written proof. The originality literature check may not find equivalent older coding-theoretic formulations.
