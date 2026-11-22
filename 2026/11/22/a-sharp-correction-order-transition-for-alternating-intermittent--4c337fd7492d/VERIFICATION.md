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

# Verification notes

The exact proof checks are substitution of the inverse-series coefficients into the two-branch composition, expansion of the \(\alpha\)-inverse-power increment, summation of \(u_j^{-\theta}\) and \(u_j^{-1}\), and summability of the displayed remainder exponent \(\eta>1\). For logarithmic regimes, the preliminary estimate \(u_n=cn+O(\log n)\) justifies the \(O(1)\) correction in harmonic sums.

Numerical comparison: execute `python3 checker.py` with standard Python; it uses bisection to produce four representative parameter pairs in both branch orders. These comparisons do not certify the infinite theorem or novelty.

External independent audit: not performed. Initial condition, parameter boundaries and no-uniformity limitations are given in RESULT.md.
