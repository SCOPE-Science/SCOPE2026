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

# Verification

Reproduce with `python checker.py` using Python 3, NumPy, SciPy and NetworkX. The script builds eight strongly regular graphs from adjacency data, obtains exact graph-parameter eigenvalues, separately computes fractional spectral powers from a numerical eigendecomposition of the Laplacian, then compares `scipy.linalg.expm` against the analytic projector formulas. It checks the sign regimes on edges/nonedges/diagonals, critical roots, the optimizer relation, near-critical scaling and high-exponent scaling.

Observed run: 568 independent matrix-time comparisons; 32 finite scale checks; 800 grid checks that the analytically characterized critical exponent dominates sampled competitors. All checks passed. The numerical eigenvalues near zero are thresholded at \(10^{-9}\) solely to avoid floating-point fractional-power artifacts for the exact zero eigenvalue. Matrices are at most 25 by 25. The analytical proof of global uniqueness and exact endpoints is in RESULT.md; finite computations alone cannot certify all graphs or all exponents. No external independent audit has been performed.
