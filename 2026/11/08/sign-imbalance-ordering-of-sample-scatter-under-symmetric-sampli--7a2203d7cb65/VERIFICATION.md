---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Write Xi=epsilon_i Yi with independent fair signs and iid positive magnitudes, fix sign sum h and use Q=T−S²/n. Conditional cumulants of S (ah,nv,hr,nw) and Cov(T,S²)=n(f−b²)+2(h²−n)a(c−ab) yield affine dependence on h². Total-variance closure fixes intercept V−A+Bn with V=(n−1)/n[(n−1)f−(n−3)b²], A=2a⁴(n−1)/n. B=(4a/n²)[(n−2)E(Y(Y−a)²)+Cov(Y²,Y)], and independent-copy identity Cov(Y²,Y)=1/2 E[(Y−Yprime)²(Y+Yprime)] ensures strict positivity unless Y constant. K binomial fair gives Var(h²)=2n(n−1), so explained fraction=2a⁴/[(n−1)f−(n−3)b²]. Independently exact-enumerated conditional means and variances for n2..5 under a two-atom positive-magnitude law; inspected all checker.py enumeration and the full analytic proof. Checks finite only; derivation is all-n.

## originality

PASS

Conditional sign-count mean, variance monotonicity, exact nonlinear explained-variance ratio are not provided by classical sign-test references or the inspected spacing-based symmetry test. Another published result on sign-run count versus scatter uses runs after a sign-blind ordering, not K or its squared imbalance. General quadratic-form fourth-moment formulas may give these identities as specialized consequences, still requiring a nontrivial conditional projection; this is an explicit priority risk.

## value

PASS

A zero covariance between scatter and the raw sign count masks nonlinear predictability from imbalance h². Exact distribution-uniform conditional dispersion monotonicity, limiting constant-magnitude equality, and Gaussian explained fraction 4/(π²n) clarify a natural statistical question about sign information and scale. This is an all-n structural statement rather than a generic unconditioned variance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
