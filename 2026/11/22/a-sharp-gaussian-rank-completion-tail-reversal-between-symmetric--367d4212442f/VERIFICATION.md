---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

In an orthonormal kernel/range basis, the independent update has blocks XY, Xv^T, Yu, C+uv^T. Schur elimination at XY!=0 gives exactly C, hence determinant XY det(C) and the stated inverse, with upper-left block (1+v^T C^{-1}u)/(XY). Taking q=p gives the symmetric formula and determinant; the sum of the two positive-semidefinite forms is positive definite when X!=0. To check the small-ball constant without a Bessel formula, integrate the half-normal density of |X| against P(|Y|<eps/x). For eps<=x<=1, expand the half-normal density at zero and the half-normal CDF at eps/x: the main integral is (2/pi)eps log(1/eps), both Taylor errors integrate to O(eps), and the two complementary intervals contribute O(eps). The one-normal square law follows directly from the CDF. The top-left numerators are independent of the kernel Gaussians and have all positive moments. For Z=1+v^T C^{-1}u, restriction to |Z|<=sqrt(R) gives the leading factor E|Z| after expanding the small-ball function; E[|Z| |log |Z||] is finite and the discarded probability is O(R^{-2}) by a fourth-moment bound. For the symmetric numerator dominated convergence applies using the half-normal CDF bound and E sqrt(1+u^T C^{-1}u)<infinity. The remaining blocks have O(1/R) tails by conditioning on u or v and the CDF bound; triangle inequalities at thresholds (1±eta)R and then eta->0 transfer the two exact asymptotics to the full operator norm. The constants are strictly positive, and tail integration gives divergence at the two endpoints as well as the sharp open moment intervals. The exceedance ratio then follows. All arguments are at fixed A and dimension.

## originality

PASS

The nonsingularity of rank completion and the block inverse are covered by randomized rank-completion work. The product-normal density is classical. The specific result here is the full-matrix inverse-norm comparison at fixed corank one, with exact range-dependent prefactors and different positive moment cutoffs. In the inspected sources the older general bounds do not give the exact dominant term for both schemes or its tail and moments. The exact catalogue hit is the frozen record itself and is not independent coverage.

## value

PASS

The theorem quantifies a design tradeoff that almost-sure rank completion misses: positive-definite symmetry makes the null-coordinate amplification substantially heavier at high thresholds. The conclusion is spectrum-independent at the exponent level while giving spectrum-dependent exact constants, and separates finite fractional moments. This is useful for comparing rare inverse amplification without conflating it with typical behavior or condition-number ordering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
