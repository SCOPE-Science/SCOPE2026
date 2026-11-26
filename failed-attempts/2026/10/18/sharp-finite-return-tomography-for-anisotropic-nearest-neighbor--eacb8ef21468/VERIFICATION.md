---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Fourier inversion averages exp(z Σ h_j cos θ_j) into ∏ I₀(h_j z). Writing I₀=exp(u) gives u''+u'/z+(u')²=1; comparing z^(2m−2) yields the stated recurrence with coefficient 4m² on c_m. The negative sign and common sign of the products inductively give nonzero alternating c_m. Thus a prefix of observed returns and the corresponding even power sums determine each other by triangular formal logarithm and exponential. Newton identities give all but the constant of Q(t)=∏(t+h_j²). In the beta-integral normalization, increasing that constant between two admissible candidates decreases Q'/Q at every t>0 because the positive derivative is unchanged. This strictly increases the sum of square roots, forbidding a second choice with sum 1; no simple-root hypothesis is used here. For d−2 moments the tangent constraint matrix also includes the normalization row. A dependence would yield a nonzero polynomial with at most d−1 terms vanishing at d distinct positive weights, forbidden by Descartes. The implicit function theorem gives a one-dimensional local fiber in the open simplex, with nonpermutation points, and the d=2 no-data case is immediate. First-return renewal is triangular, including in transient dimensions. Independently the d=3 witness checks via r₂=Σh_j²/2 and r₄=3(Σh_j²)²/4−3Σh_j⁴/8, giving 31/144 for both r₂ and 961/9216 versus 865/9216 for r₄. The support script was inspected, not executed.

## originality

FAIL

The central sharp identifiability finding is covered via the known nonnegative power-sum recovery theorem and rank calculation in Melánová, Sturmfels and Winter, arXiv:2106.13981. The return prefix is a triangular reparameterization of the even power sums; normalization contributes the moment of exponent 1. Proposition 24 covers the resulting d distinct positive integer exponents {1,2,4,…,2(d−1)} and does not require distinct coordinates in its stated conclusion. With the last exponent omitted, their generalized Vandermonde–Schur Jacobian calculation implies full row rank at positive pairwise distinct coordinates, giving precisely the claimed local fiber by the implicit function theorem. The probability-language statement, renewal transfer, and direct integral proof of uniqueness are useful, but not a distinct sharp identifiability theorem once that moment equivalence is made explicit. The decision is by stronger coverage, not absence of a novelty citation or a conflict with finite-range examples.

## value

PASS

There is intrinsic value in the constructive last-coefficient reduction: the return data determine the leading polynomial coefficients and the simplex constraint gives a strictly monotone scalar test on admissible constant terms, including repeated weights. It gives a specific route for reconstruction rather than only an abstract injectivity assertion. The distinction between that constructive mechanism and the already implied sharp cutoff is material to this value assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
