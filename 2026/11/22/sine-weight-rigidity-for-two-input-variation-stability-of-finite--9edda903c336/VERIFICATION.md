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

# Reproducible verification

The analytical proof in `RESULT.md` establishes the exact variation norm for each positive weight vector and the sharp global sine minimax theorem for every finite length. `CHECK.py` requires only Python 3 standard libraries. From the containing directory, run `python CHECK.py`.

The checker exhaustively enumerates every binary cut of each cardinality for path sizes 2 through 11 and checks that central consecutive boundaries exist and have the predicted sine-weight value. It then checks arbitrary positive rational weights, exact step-permutation norms and two-input sorting inequalities over 8,330 rational tests, plus an explicit strict-chamber pair whose ratio attains the maximum-cut norm. The output must conclude with `ALL_SORTING_VARIATION_CERTIFICATES_PASS`.

Numerical trigonometric tolerance \(10^{-10}\) applies only to the sine constants. The comparison and uniqueness theorems are proved symbolically for arbitrary \(n\) using the minimum component of \(w_i/\sin(\pi i/n)\) and the full-support central row of the cut matrix; they are not inferred from enumeration. Historical novelty is supported by documented comparisons, not formally or independently certified.
