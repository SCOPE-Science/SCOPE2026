---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Orthonormal real-mode projection gives independent OU noise with variance rate 2D and drift νq_i². At stationarity the common age is Exp(r), and the conditional coordinate variance is v_i(A)=(2D/b_i)(1−exp(−b_i A)). Conditional means of unsquared coordinates are zero and distinct coordinates are conditionally independent. For squares of distinct coordinates (including a sine/cosine pair at the same wavenumber), total covariance leaves only w_iw_j Cov(v_i(A),v_j(A)). For a single squared coordinate's variance there would also be 2w_i²E[v_i(A)²]. Subtracting Laplace moments r/(r+b_i+b_j)−r²/((r+b_i)(r+b_j)) gives numerator r b_i b_j over the common denominator. The resulting kernel is a Cauchy matrix up to positive row and column scalings, taking x_i=b_i and y_j=r+b_j in the classical determinant formula. Both Vandermondes are positive on ordered distinct indices and no denominator vanishes, proving all minors and full rank. Normalization gives ρ²=1−(b_i−b_j)²/(r+b_i+b_j)², hence strict increase for i≠j, the limits, and the inverse on the indicated range. With known L, this statistic is a function of r/(2ν), so recovering the absolute r from it requires calibrating ν.

## originality

FAIL

The decisive overlapping Resultary theorem 581ff25262aa explicitly gives the pairwise stationary covariance of quadratic energies for independently driven OU coordinates with a common origin-reset Poisson clock. It allows distinct labels with identical relaxation frequencies, so it already yields every entry, including the cross-sine/cosine diagonal when those two modes are taken as the labels. With λ_i=νq_i², D_i=D, ω_i=b_i and H_i=λ_iX_i²/2, multiply its pair formula by (2w_i/λ_i)(2w_j/λ_j). One obtains the identical kernel; there are at least four real coordinates in the claimed cutoffs, so the source hypothesis of at least three labels causes no restriction. Cauchy's determinant identity applies directly to that prior formula after scaling out u_i and u_j. The proposed inverse is the one-step normalization and solution of the resulting two-by-two ratio, not a separate unresolved theorem. This rejects substantive originality based on exact statement-level coverage and deductions, not chronological priority from same-day dating.

## value

FAIL

The spectral calibration is a useful interpretation: it makes clear how to measure a latent covariance diagonal without mistaking a raw energy variance for that diagonal. But after the verified heterogeneous OU pair kernel the sine/cosine identification, classical minor product, and one-pair algebraic inverse are direct consequences. The frozen result does not establish additional scientific content such as a recovery result with unobserved quadratures, robust finite-data identification, or a new positivity mechanism; one is not required in general, but without a substantive remainder this particular specialization and normalization do not clear the value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
