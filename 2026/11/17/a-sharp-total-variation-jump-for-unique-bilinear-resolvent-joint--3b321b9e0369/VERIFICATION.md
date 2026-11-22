---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For all a>d>0,b>e>0 with r=d/a+e/b<1 and 0<=c<de, the rank-one parametrization yields det C_c=ab c, tr C_c=bd+ae, PSD completion. The 2x2 adjugate identity splits the moment resolvent into K0,c mu_c + K1 nu1,c + K2,c nu2,c. A geometric mixture of independent gammas supplies the scalar Laplace transform (1+dx+ey+cxy)^-1; at c=0 mu0 is supported on the exponential one-dimensional curve, whereas for c>0 mu_c is planar absolutely continuous. The two exponentially smoothed laws remain absolutely continuous at c=0, and their TV convergence follows by a common exponential marginal, E(X-(d/e)Y)^2=2dc/e, and shifted-exponential TV <=2|h|/a. Mutual singularity of mu_c and mu0 gives variation of K0 terms equal to sum of two operator norms, tending to 2r; remaining terms are O(sqrt c). Matrix moment convergence plus polynomial density proves weak convergence. All r in (0,1) realized by a=b=1,d=e=r/2. Finite exact matrix checks do not prove the limit.

## originality

PASS

Tian (2026) supplies the positive bilinear-resolvent completion and 3-component measure decomposition and Downton (1970) supplies background bivariate exponential laws. The assessed new statement is the exact operator-valued total-variation discontinuity 2(d/a+e/b), its O(sqrt c) remainder, and weak-versus-TV contrast at rank drop. Full Tian HTML comparison found the ingredients, not the variation limit; historical probability-limit coverage remains a risk.

## value

PASS

Shows that a natural positive unique operator-valued moment problem can be perfectly weakly stable yet suffer a sharp norm discontinuity from emerging rank-one singular mass. The explicit coefficient and O(sqrt c) quantitative contrast help diagnose strength of approximation as a matrix completion loses rank; sizes fill (0,2). This is a motivated stability boundary, not merely a restatement of existence of the measure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
