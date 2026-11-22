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

The standalone script `verification/check.py` was run successfully with Python, SymPy, and mpmath and reported **69 checks passed**. It verified the exact rational contrast polynomial and its discriminant, the shifted quartic, both endpoint values, the double root and square-root onset, the first two interior roots at support ratio six, direct finite-sample U-statistic identities, alternative projection variances, 5% Gaussian limiting rejection probabilities, and direct survival-integral quadrature against exact integration.

The proof of uniqueness of the threshold and root counts uses Descartes' rule and continuity of polynomial roots. The stochastic conclusion is proved via the order-three U-statistic central limit theorem and Slutsky's theorem. Numerical checks alone do not establish these infinite-parameter and large-sample statements.

Verified rounded values: threshold `4.180098403603496010737`, double weight `0.5977073861451475403038`, onset coefficient `0.2502581513893773405`. At ratio six, the two blind weights are approximately `0.334684697337449837` and `0.856910197349909709`. The corresponding normalized projected variances are `0.601031193685939689` and `1.41841748723473935`. Their nominal-5%-test limiting rejection rates are `0.0288689045081560778` and `0.108360616550849108`.

The later journal edition's full text was unavailable for historical comparison; no independent expert validation has been performed.
