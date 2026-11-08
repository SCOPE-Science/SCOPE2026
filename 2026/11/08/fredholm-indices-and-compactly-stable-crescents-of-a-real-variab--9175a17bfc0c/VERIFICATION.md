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

# Verification evidence and limits

The analytical proof checks the change-of-variables isometry, the exact differential coefficient and its two limits, invertibility of the first-order operator, compactness of the coefficient perturbation from \(W^{1,p}\) to \(L^p\), the three half-line matching cases, and non-Fredholmness on both critical lines and at zero. Compact stability follows from the ordinary Fredholm index theorem.

Run `python checker.py` in an environment with Python 3, SciPy and NumPy available. The completed check reported `PASS: 118 algebraic, integral and geometric diagnostics`. Its quadratures test sample formulas and do not prove the infinite-dimensional claims. Neither independent audit nor external formal certification has been performed. The original preprint's first public release is established from the arXiv submission history, not an inferred journal date.
