---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In the stated independent Gaussian observation-noise model, integration of the fixed Matérn kernel gives prior variance 8/e−2 and equal observation cross-covariances m(s). The observation covariance has eigenvalue 1+η+k(s) on the equal-coordinate direction and remains nonsingular at s=0 with two independent errors. Thus the removed variance is 2m(s)^2/(1+η+k(s)). With m'=−su and k'=−4s exp(−2s), its log derivative is 2su(T−η)/(m(1+η+k)), so sign is decided by one threshold function. Differentiation gives T'=2 exp(−2s)[s−(m/u)(2+u'/u)]. To validate the uniform bounds, the terms in the cosh tail starting with s^4/24 have ratio at most 1/120 on [0,1/2]; thus that tail is below s^4/20 for s>0. With sinh(s)/s>=1+s²/6 this gives u>=139 exp(−1/2)/160; the exact power series gives u<=exp(−1/2). Dropping the positive derivative term in u' gives u'>−2 exp(−1/2)sinh(1/2), with sinh(1/2)<0.522 by its series. This gives u'/u>−1.21. Also m>=2−3/e>0.89, so su/m<0.35 and T'<0. The endpoint values are T(0)=8√e−12>0 and T(1/2)=(1+2e−e²)/(e(e−2))<0. The objective strictly peaks at the unique threshold crossing or, at and above critical noise, at zero, without a tied positive separation. Since m and u are even near zero and k'(0)=0, the right derivative T'(0)=−4m(0)/u(0)=−(16√e−20) verifies the linear inversion. In the separately authored numerical calculation at η=0.1, s=0.234026645898 and posterior variances 0.047354068218 (optimum) and 0.051835871485 (collision) agreed with the finding; independent integration and the explicit matrix inverse corroborate the formulas.

## originality

PASS

The distinctive result is the exact finite-noise location switch and its linear onset for the stated Matérn-3/2 geometry, not the usual Bayesian-quadrature variance formula or the general existence of a replication phenomenon. The nearest different collision result uses a squared-exponential kernel, Gaussian integration measure, and a precision budget, with square-root rather than linear onset. The distinct exponential and bridge analogues have no finite noise collision.

## value

PASS

The replication decision is meaningful for a natural regularized integral design: exactly two noisy evaluations can be spent either at distinct sites or as two independent midpoint observations. Knowing the exact noise boundary and proving a globally unique paired optimizer gives more than a local stability test. The linear collapse distinguishes the particular Matérn covariance from smoother analogues and gives a quantitative law near the switch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
