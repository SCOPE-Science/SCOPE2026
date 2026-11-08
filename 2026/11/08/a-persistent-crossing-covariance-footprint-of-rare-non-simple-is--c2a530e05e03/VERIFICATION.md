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

# Reproducibility and limits

Use Python 3 standard library: `python3 verify.py`. The checker enumerates complete matchings for \(2\le n\le7\), calculates intersection-graph crossings and isolated chords independently of the analytic expression, and asserts the exact rational covariance against the conditional split formula. It also tests crossing variances, isolated-count expectations, the conditional convolution of the two arcs for \(2\le n\le5\), isolation-weight ratios, and rational large-size diagnostics.

**Observed result:** 1,304 exact assertions passed; largest complete enumeration contained 135,135 matchings at \(n=7\). The conditional enumeration and arithmetic are finite checks and do **not** certify the infinite asymptotic claims. Those follow from the explicit ratio/tail proof and the \(L^2\) decomposition in RESULT.md. The classical crossing variance is also cited from Flajolet–Noy (2000), Theorem 3.

No independent audit or external formal certification has been conducted.
