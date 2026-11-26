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

For each coordinate the product L2 norm is at most (a^2+s)^(k/2), so the series tail tends uniformly to zero and the mean is the target inverse times b. For a branch parameter c, centering gives X_c=(a+c epsilon)X'_c+c mu epsilon with mu=(1-a)^-1, and the primed pair independent of epsilon. For c,d the covariance solves K_cd=(a^2+cds)K_cd+cds mu^2, so inserting c,d=1,-tau reproduces all three terms and the factor 1/4. Squared Euclidean risk adds coordinates even with dependent noise coordinates. The bracket derivative is 2B[tau/(B-s tau^2)^2-1/(B+s tau)^2] and is strictly increasing for an active mode, negative at 0 and positive at 1. Positive weighted sums retain these signs and strict convexity. Only one weighted active mode uses the quartic: square-rooting the stationary equation with positive denominators gives the stated polynomial. Its derivative in u is positive; its expansion at nu=0 and its factorization at nu=1 give the two boundaries. The normalized risks at high noise tend to 1/4 at the optimum and 1/2 at full mirror. Uniform moment convergence on the compact parameter interval gives consistency of finite-depth minimizers, with a tau-independent truncation bias. Read VERIFICATION.md and verify.py without executing supplied code. Ancillary erratum: the quoted variances in the scalar example are correct, but full mirroring is about 25.8% above the optimum; 20.5% is the reduction relative to full mirroring. That reversed percentage base does not affect the theorem, example optimum, or risks.

## originality

PASS

The estimator, full-reflection odd cancellation, and general affine-recursion covariance machinery are verified prior coverage. The supported distinct result is the universal variance-optimal mirror-strength selection theorem within the stated equal-weight exact-reference commuting family, including the one-mode calibration and sharp boundary ratios, not a claim to new perpetuity covariance theory. No inspected prior result determines that selection or implies it by a reduction of an existing optimizer theorem.

## value

PASS

The prior default mirror strength is natural for cancellation, but cancellation and variance minimization are different objectives. A universal strict interior choice over the entire exact-reference commuting family, with a sharp noise-dependent calibration and an exact separation from full mirroring at the stability boundary, gives a usable benchmark for a naturally tunable estimator rather than an arbitrary finite test. No benefit for wall-clock cost, noncommuting systems, skewness, or training metrics is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
