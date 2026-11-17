---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For every n>=2 uniform Dirichlet simplex coordinates, the conditional coordinate decomposition M_n=(1-X_1)Y_{n-1}+R_n yields n Cov(M_n,K_n(t))=1-eta_n(t)-(1-t)^(n-1)(1+nt H_{n-1}), eta=n² E[R_n 1_{X_1<=t}]. The exponential representation bounds eta by n²[(2/e)^n+exp(-n exp(-2nt))], which is o(1) at nt=loglog n+logloglog n+z; remaining product ->e^-z. Convexity of h_n(t)=E[M_n|X_1>t] gives unique interior zero and the profile brackets its two-log position. Independent rational small-dimensional identity and window-sign checks reproduce normalization; finite n is not an infinite proof.

## originality

FAIL

FAIL: an earlier October 13 full primary theorem proves the same unique crossing for the identical uniform Dirichlet spacings and exactly the same two-log centering. Crucially its proof contains a UNIFORM estimate p_n(s/n)=e^s/n(1+o(1)) for 0<=s<=3loglog n and running average R_n(s/n)=(e^s-1)/(n s)(1+o(1)); its exact identity C_n(t)=n t(1-t)^(n-1)(R_n(t/(1-t))-H_n/n) then, with s=loglog n+logloglog n+z, immediately gives n C_n(t)->1-e^-z. Thus the apparently new full crossover is a direct specialization of already established stronger quantitative proof, not just a matching center. An October 18 paper independently supplies exact finite formula and unique sign switch.

## value

FAIL

FAIL as a distinct contribution: the critical center is previously proved for the same exact object, and the stated 1-e^-z profile follows by one algebraic substitution into a uniform asymptotic already established in the primary earlier proof. Mathematically correct but mechanically implied; no independent structural/unknown invariant remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
