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

The exact stated eigenvalue, minimum and case split are correct. For the assumed K=r Phi D Phi, the orthogonal split is the span of the hub and peripheral mean versus peripheral zero-sum. On the latter the block is r C^2 with norm at most r. The all-ones Rayleigh quotient r(1+q/M) makes the two-dimensional block dominant and gives the minimum bound, where q=zeta-1. In the eigenbasis of the hub block of Phi its normalized next-generation matrix is diag(1,d^2)+(q/M)(1,sqrt(k)d)(1,sqrt(k)d)^T, with d=1-Mp, up to orientation of the second vector. At d=0 the minimum is attained, and a nonzero off-diagonal entry excludes equality elsewhere for q>0. The trace and determinant are T and zeta d^2. For r<1 the positive definite background I-r diag(1,d^2) turns the rank-one downdate into a scalar inertia test: chi=(rq/M)(1/(1-r)+kd^2/(1-rd^2)), and chi<,=,>1 is precisely the respective spectral comparison. Solving yields the displayed H, whose denominator is positive because q<q_c implies M(1-r)-rq>0 and M zeta(1-r)-q=[M(1-r)-rq]+k(1-r)q. The proof's line 89 misprints chi(1) as rq; it is rq/(1-r). For 0<q<=(1-r)/r this gives chi(d^2)<chi(1)<=1 since d^2<1, and for q=0 chi is zero directly. This local arithmetic error does not invalidate the Finding, which follows from the preceding exact test. At r>=1 the Rayleigh lower bound suffices; homogeneous zeta=1 follows from stochasticity. The frozen checker was inspected, not executed.

## originality

FAIL

Earlier Resultary record 3575e4cfa8c0 gives a stronger rank-one threshold/equality criterion for the same K over every symmetric stochastic block and the complete equality criterion for the same global lower bound. In the uniform-hub family its spectral sum has only the homogeneous and hub-contrast modes. Evaluating the resulting equality criterion at a freely varied scaling r'=1/lambda recovers not just the threshold but the entire dominant eigenvalue and exact radical by a two-term quadratic. Thus the quantitative and qualitative findings are mechanically implied by the earlier result, not merely similar in terminology. The later exact quotient result confirms overlap without establishing earlier priority for itself.

## value

FAIL

The network question is meaningful, and the quotient is a useful exposition. As a distinct finding, however, the stated optimizer, threshold and radical are routine evaluation of the known rank-one result in a two-mode special case. There is no substantially new exact fact or separate remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
