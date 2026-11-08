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

# Verification and reproducibility

The analytical argument establishes three independent statements: the analytic-series criterion for the original shift, the analytic-series criterion for its Cauchy dual, and the exact singular-value multiset of the compact perturbation. Comparison of the two series yields the sharp Wold transition; comparison of two spine sums and one tooth sum yields the sharp Schatten threshold and asymptotic constant. No finite computation is used to infer divergence or compactness.

Run `python3 checker.py` in the directory containing this document. The Python script requires only the standard library and performs 17,129 finite checks at sampled parameters, including positive and nonpositive spine levels, primal/dual path products, matrix-column norms, and finite Schatten sums. These checks are consistency tests, not exhaustive verification of an infinite result.

The source of the infinite-dimensional Wold characterization is Chavan–Trivedi, arXiv:2501.01296, Theorem 1.3. Its hypotheses are verified explicitly in the proof: the tree is rootless and leafless, the weights are positive, the shift is bounded and left invertible, and both required series are computed as exact expressions. The application does not assume that compact perturbations preserve the Wold property.

The construction is limited to this rootless comb family and does not establish a universal threshold for all trees. No independent audit has been performed.
