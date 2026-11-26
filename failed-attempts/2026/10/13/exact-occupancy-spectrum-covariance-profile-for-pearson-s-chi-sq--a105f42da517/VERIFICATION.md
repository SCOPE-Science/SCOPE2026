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

Writing C for the colliding sample-pair count gives Q=m-n+2mC/n. Conditional on N_1=r, the expected collisions are binom(r,2)+binom(n-r,2)/(m-1), while unconditional mean is binom(n,2)/m. Centering and multiplying by m p_r and 2m/n gives the claimed polynomial covariance including r=0 and r=n. Distinct pair-collision indicators are pairwise independent even when they share one draw under uniform sampling, giving the stated Var(Q). The two-cell multinomial mass gives Var(K_r), with 0^0=1 when m=2 and n=2r. For the fixed-load limit, put lambda_m=n/m. The ratio p_rr/p_r^2 equals (n-r)_r/(n)_r times (1-2/m)^(n-2r)/(1-1/m)^(2(n-r)), with falling factorials. Its logarithm is [2r-lambda_m-r^2/lambda_m]/m+O(m^-2), giving the claimed limiting variance with p_r converging to pi_r. The limiting variance is strictly positive: it is the variance of the residual after linearly projecting 1{Z=r} on a Poisson(lambda) variable Z, and this indicator is not affine on the full nonnegative-integer support. The covariance polynomial limit and Var(Q)/m→2 give the correlation; for r=1 the lower formal zero at lambda=0 is outside the stipulated positive-load regime. Independent replay: python3 -I -B /workspace/audit_replays/frozen_math.py 4, with 312 exact frequency strata via multinomial compositions for 2<=m<=7 and 2<=n<=9.

## originality

FAIL

The entire finite covariance is a direct specialization of a distinct same-day indexed theorem for all additive cell scores. The October 18 indexed collision theorem also gives the same profile, including exact signs, through the affine relation between Q and pair collisions. No within-date order or historical priority is inferred. The fixed-load correlation is a direct normalization of this already covered covariance using the binomial/two-cell variance expansion and exact Pearson variance, not a separate uncovered mechanism.

## value

FAIL

The load-dependent signs are interpretable for goodness-of-fit analysis, but the same exact profile and threshold behavior are already covered by the indexed curvature and collision identities. Expressing the result as a correlation by marginal variance normalization adds no distinct boundary, limit mechanism, or inferential conclusion. This is useful exposition of an existing relation, not a separate unknown exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
