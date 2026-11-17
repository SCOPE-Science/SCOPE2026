---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

PASS: Direct Dirichlet-multinomial one- and two-category masses yield Cov(U0,Ur)=m p0 pr [(m-1)Q_N-m]. The exact Q_N ratio has successive factor 1-alpha(alpha+r)/((N-r+(m-1)alpha)(N+(m-1)alpha)), strictly between 0 and 1. At N=r the factor gives positive aggregate covariance for r>=2, and the limiting Q is strictly <1; hence the unique real sign change by gamma/digamma monotonicity. For alpha=1 the factor simplifies exactly to [m(r-1)+2-2N]/(N-r+m-2), giving critical N=[m(r-1)+2]/2. Independent complete weak-composition enumeration for m=3..5,r=2..4,N up to 11 reproduced every sign and direct covariance; infinite proof is analytic, not merely finite tests.

## originality

FAIL

FAIL: The 2026-10-13 published symmetric Dirichlet-multinomial theorem already proves the identical aggregate unseen/doubleton r=2 sign crossing and alpha=1 threshold. A stronger 2026-10-26 theorem for arbitrary concentrations and every r>=1 gives the exact labeled missing-versus-r joint probability ratio Q_N, its strict monotone recurrence, real crossing and unit-shape identity. Summing exchangeable pair indicators and subtracting same-category exclusion mechanically changes their criterion Q=1 to (m-1)Q=m, reproducing the entire submitted aggregate arbitrary-r theorem and alpha=1 formula. The new variation is a routine algebraic corollary of disclosed general formulas, not an independent mathematical discovery.

## value

FAIL

FAIL for a separately valuable contribution beyond these priors: missing and fixed-frequency aggregate counts are natural observables, but r=2 had already been solved exactly and the all-r Q ratio, monotonicity and unit-shape algebra were already explicit in a broader labeled-category theorem. Exchangeable summation with a single same-label exclusion yields the submitted threshold by a one-line calculation; the remaining multinomial limit is a direct limit of that formula. Reproducibility/novel presentation alone does not make this mechanical consequence an independently needed result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
