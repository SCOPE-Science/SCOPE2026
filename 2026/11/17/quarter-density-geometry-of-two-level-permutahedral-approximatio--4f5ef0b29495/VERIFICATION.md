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

# Reproducibility and mathematical verification

Run `python verify.py` with Python 3.10+, NumPy, and SciPy. `verify.py` is entirely standalone and uses no external input files.

The exact rational check covers all \(3\le n\le25\), \(1\le k<n\), totaling 299 integer pairs; it validates the shift balance, rational squared distances, cap inequalities, ordered residual pattern, symmetry in \(k\leftrightarrow n-k\), and supporting-hyperplane signs against sampled vertices of the capped-sum hypersimplex. The full permutation residual partition is enumerated in all 20 cases \(3\le n\le7\), checking the predicted \(n!/m!\) groups of \(m!\) vertices apiece. Eighteen large-dimensional comparisons test the explicit two-branch asymptotic formula. A separate SciPy SLSQP implementation solves 35 strictly convex quadratic programs in dimensions 3 through 9; the largest observed objective gap is below \(4\cdot10^{-14}\).

The all-dimensional Hausdorff identity, union-of-faces equality characterization, and limiting third-derivative transition are analytic theorems proved in `RESULT.md`, not inferred solely from finite tests. The code does not provide an external or independent mathematical audit. Source dates are the original preprint submission dates, not later revision dates.
