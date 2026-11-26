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

The Fourier coefficients at k≠0 are E X^|k|, so Parseval contributes exactly 2 times the sum of squared differences of positive-frequency coefficients. Geometric summation gives (7). The mixture coefficients are bounded by R^k with R<1, justifying differentiation on compact t intervals and divergence at t→1. The derivative has the sign of 1-H(t), with H(t)=E[X(1-t²)^2/(t(1-tX)^2)]. For every x>0, the log derivative of the integrand is bounded above by -4t/(1-t²)-1/t+2/(1-t)=(t-1)/(t(1+t))<0. Positive mean and support away from one give endpoint limits infinity and zero, proving one strictly minimizing crossing; a point mass is fitted exactly, including at zero. The positive first and second derivatives of g_t(x)=x/(1-tx)^2 give the strict mean/support bounds at t=m and t=sup supp μ. For fixed t>0, strict convex-order improvement follows also by integrating g_t''(z)>0 against the difference of the two call functions E[(X-z)_+]; those continuous functions are ordered and cannot agree identically for distinct laws. Ordered decreasing crossings give the strict radius order. At (m,0) the stationary equation derivative in t is (1+m²)/(1-m²)^3 and its second derivative in δ is -2m(2+m²)Var(Y)/(1-m²)^4; the centered first derivative is zero. Uniform smoothness for bounded Y gives the quadratic coefficient and cubic remainder. In the boundary limit ε² times the equation has denominators τ(2-ετ) and τ+A-ετA, and τ stays in the positive compact depth interval by the radius bounds. The limiting 4τ² E[(τ+A)^(-2)] increases strictly from 0 to 4 with positive derivative. The implicit-function estimate gives τ_ε-τ_ν=O(ε). At the actual lower support endpoint the expression is strictly below one for a nonpoint law, and at τ=E A it is strictly above one by Jensen. The three terms in (7) give, respectively, the coefficients 1/τ, -4 E[1/(τ+A)], and 2 E[1/(A+A′)] at order 1/ε. Their combination is the squared-Laplace-transform integral with factor 2, so the constant is zero only for the exact-fit point mass. Independent rational bisection of 2τ²[(τ+1)^2+(τ+3)^2]=[(τ+1)(τ+3)]^2 on [1,3], with risk formula 1/τ-2/(τ+1)-2/(τ+3)+7/12, reproduced τ=1.601135942871122 and leading risk 0.0043198140280341 for the example.

## originality

PASS

Exclude the already credited two-component wrapped-Cauchy Fourier objective and stationary equation. The inspected comparisons do not cover the arbitrary common-center mixture's one-crossing uniqueness, strict convex-order law and local variance coefficient, or the sharp radius and optimized risk for a fixed compact positive depth distribution. Unavailable Bailey primary text remains an explicit priority risk, not negative evidence.

## value

PASS

The result isolates a systematic and orderable bias in a concrete mixture approximation problem: at the same mean radius, a mean-preserving spread strictly raises the fitted concentration. The boundary law quantifies when the best fit nevertheless has diverging residual with an explicit strictly positive coefficient, distinguishing genuine heterogeneity from an exactly fitted point source. These conclusions are useful beyond the prior formal stationarity equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
