---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Eliminating the hub using the zero-sum condition gives the negative distance quadratic form from the anchored matrix with entries d(o,i)^p+d(o,j)^p-d(i,j)^p. Its two arm-coordinate subspaces split into constant and mean-zero vectors. With x=2^p, y=3^p and t=sqrt(x), the fluctuation block is (x,y-1;y-1,x^2), positive definite for 0<p<2 since y-1<t^3 by strict subadditivity of the p/2 power. The constant block is (A,C0;C0,xA), A=2q-(q-1)x, C0=q(1+x)-1-(q-1)y. Its factors are F=tA+C0 and G=tA-C0. Independent sign checks give F(1)=2+2 sqrt(2), F'<0 for p>=1 and F(p_A)<0: 2*3^p-4^p-2 is strictly concave on [1,2] and vanishes at its endpoints. For 1<p<2 and F>=0, the real arm count lies between 0 and the root count Q(p), below the count x/(x-2) at which A vanishes; G is affine in the count, positive at 0 by subadditivity and at Q(p) because it equals 2tA there. Thus only one radial direction becomes null, namely (t,1); for all p above the root its quadratic form in the constant block is 2tF<0. Strictness below 1 follows from Li–Weston (or the p=0 matrix directly there). Centering gives affine ranks 2q and 2q-1, and q=2 is a path whose endpoint 2 follows from its line embedding and the three-point second-difference witness above 2. The root decreases in q since 3^p+t^3>(1+t)^2 for p>1. Differentiation at (p,1/q)=(1,0) gives the stated C=1.2476366340867857. The frozen numerical checker is corroboration, not the basis for the universal sign or rank claims.

## originality

FAIL

A distinct indexed record gives the mathematically equivalent whole classification, including the threshold, endpoint degeneracy, dimension drop, strict monotone dependence, and the same asymptotic constant. This is demonstrable overlap, not a finding about which author or record was first. No distinct residual claim was established that would justify a repair.

## value

FAIL

The underlying subdivision question is well motivated and its exact classification is useful. As a distinct result, however, this record presents no independently needed exact fact beyond the equivalent indexed threshold, rank transition and branching asymptotic; the unsubdivided-star comparison is an immediate consequence of their common root interval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
