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

The accompanying `CHECK.py` uses Python standard-library modules only. From the same directory run `python CHECK.py`. It exhaustively enumerates the \(C_n^2\) ordered pairs of noncrossing matchings for each \(1\le n\le7\) and computes both small-loop counts directly from the independent matching sets. The exact joint falling-factorial-moment identity is verified for every \((r,s)\) with \(r+2s\le n\) through \(n=6\), and nine more moments for \(n=7\); the exact rational covariance and its strict sign are checked for \(3\le n\le7\). The checker reports 68 passing assertions.

The analytic proof is in `RESULT.md`: forced-component deletion for arbitrary \((r,s)\), positivity of a cubic polynomial for the finite covariance, uniform high-order factorial-moment expansion for \(r+s=O(\sqrt n)\), and application of the independently published multivariate normality criterion. Exhaustive finite testing is not a proof of the infinite limit. The calculation does not address nonconsecutive four-site loop supports or arbitrary component shapes.
