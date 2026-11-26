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

The frozen equation (1) is not the covariance defect for an arbitrary noncentered input: it omits Cov(P(U) mu). For example, with lambda=1, h=1/2, equally likely stages 0 and 1, and input mean and variance both 1, the omitted variance is 1/64. The centred-only argument also did not explain why an arbitrary finite-variance candidate was covered. The full replacement adds the positive-semidefinite term. In an eigenmode t>1 the centered part is strictly positive even without it; t=1 forces U=1, and then every eigenmode must have t=1, giving the identity. For all t_j<1, stationarity of the mean forces zero because each mean multiplier is strictly less than one. Subtracting the covariance constraints for distinct modes then forces E U²=0 and gives a contradiction. In isotropy, bounded Gaussian innovation moments and a uniform multiplier bound below one give the unique stationary law and all finite moments. Its fourth-moment recursion gives (1-E R^4) cumulant_4 = 3 Var(R²/lambda+s); strict monotonicity of q_t makes this positive exactly for nonconstant calibrated stages. The unique deterministic root preserves the full Gaussian by the affine Gaussian update. Equal innovation covariances give the exact point-start W2 factor, and differentiating 2-t-sqrt(1-t²) gives the unique per-step optimum. An independent rational check reproduced the random-stage cumulant 3321/10498, the deterministic stage 5/9 at t=3/5, and a residual 3/49 at the second curvature in a two-mode test. The repair retains the full original classification and fixes its proof for uncentred candidates.

## originality

PASS

For the surviving theorem the stochastic update with a uniform stage is known, and covariance versus Gaussianity is a known distinction in other random integrators. The supported contribution is the exact arbitrary-stage classification of this shared-increment map, its cumulant identity and the associated optimal deterministic calibration. The repair changes the proof of necessity, not the claim compared for priority.

## value

PASS

For a standard explicit randomized midpoint update, a sharp harmonic calibration limit decides when changing the stage law can fix covariance at all. It then distinguishes variance correction from exact sampling and gives the exact best per-step rate among Gaussian-preserving choices. This is valuable for interpreting Gaussian benchmarks without suggesting accuracy for nonlinear potentials or optimality per unit computation or physical time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
