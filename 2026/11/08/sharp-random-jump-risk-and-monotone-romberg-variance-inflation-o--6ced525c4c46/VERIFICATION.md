---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For f_C=1_{x>C}, C uniform(0,1), composite trapezoid error equals h B_1({NC}). Splitting a coarse phase into integer fine subdivisions shows Cov(E_i,E_j)=min(h_i,h_j)²/12. Successive coarsening differences are orthogonal, giving the exact sum-of-squares risk for constant-exact coefficients and unique finest-only minimizer. Given the finest-grid sample vector the jump remains uniformly distributed within one cell, and T_finest is its conditional-mean integral, proving optimality among all measurable finite-MSE estimators including independent randomization. The geometric Richardson coefficients follow from Lagrange interpolation at even-power nodes. With q=r^(−2)≤1/4, the signed tails alternate with decreasing absolute coefficients; differences on increasing depth have same initial tail sign and strictly positive magnitude, so every old tail square strictly increases and one new term appears. Uniform q^{j(j+1)/2} domination yields a finite exact infinite-depth limit; for dyadic r=2 the first factors 1,4/3,208/135 and limiting approximation 1.625991555. Independent exact rational finite-depth integration confirms formulas without standing in for all-depth proof.

## originality

PASS

Best of knowledge: classical Romberg even-power cancellation, positivity of collected weights and the conditional-mean property are not independently novel. The new integrated uniformly unknown jump phase covariance, fully nonparametric sample-vector MSE optimum within the specified step family, and strictly increasing normalized integer-ratio all-depth Romberg risk are not implied by the inspected known-jump correction or sample-noise sup-norm stability results. Broad numerical quadrature literature leaves some priority uncertainty.

## value

PASS

For an unknown discontinuity, smooth-function Romberg cancellation is an unreliable heuristic. The exact covariance and the strict all-depth relative risk penalty quantify a natural and important failure mode, while the conditional-mean theorem establishes a sharp information baseline. The result is a motivated statistical quadrature classification, not merely a textbook fact about extrapolation coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
