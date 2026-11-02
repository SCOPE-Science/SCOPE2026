---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The frozen six-file Git tree was independently reconstructed from the real blob SHAs and matched the assigned source SHA. The nonstandard input is Denčić--Stanković--Krstić--Damnjanović Theorem 2.1, examined in its full proof, which gives omega_r(A)=(||A||/2)[1+r c+sqrt(1-r^2)sqrt(1-c^2)] for rank-one A, c=|tr A|/||A|| in [0,1]. For complex q the scaled q-range is phase invariant, so Omega_q(A) contained in the closed disk iff omega_r(A)<=r. Rearranging gives the stated pointwise inequality for ||A||. For each 0<r<1, g(c)=rc+s sqrt(1-c^2) has g''(c)=-s(1-c^2)^(-3/2)<0 on (0,1), so its minima are exactly endpoints c=0 or c=1; when s=r the endpoints tie and no interior c minimizes. For r=1, g(c)=c, so c=0 is uniquely minimizing. Every c in [0,1] is realized by a rank-one operator on complex H of dimension>=2, using unit factors e1 and c e1+sqrt(1-c^2)e2. The equality condition c=1 gives a scalar multiple of an orthogonal rank-one projection by Cauchy--Schwarz; c=0 gives A^2=(tr A)A=0. The threshold r=s occurs only at 1/sqrt(2). The square-zero branch solves 2r/(1+sqrt(1-r^2))=1 exactly at r=4/5, and r=1 yields R1(1)=2. Strict inequalities and equality cases hold with r>0; no invalid r=0 division or claim about rank>=2 is made.

## originality

FAIL

The submitted rank-one scaled-disk envelope and both endpoint extremizer classes are mathematically contained in already published results. In particular, the complete published sharp two-sided rank-one comparison of q- and rho-numerical radii yields, on setting rho=1 (so omega_rho(T)=||T||), the exact sharp constant M_{1,r}=max{2/(1+sqrt(1-r^2)),2/(1+r)} for ||T||/omega_r(T). Because Omega_q(T) subset closed disk iff omega_r(T)<=r and positive scaling is unrestricted, the submitted supremum is exactly R_1(r)=r M_{1,r}. The comparison theorem proves endpoint maximizers: trace overlap zero (square-zero rank one) versus overlap one (scalar rank-one projection), switching exactly when r=sqrt(1-r^2), i.e. r=1/sqrt(2). Its q=1 boundary is included. Thus the whole sharp envelope, strict classifications and equality case are a direct rho=1 specialization, rather than new operator geometry; both relevant records have public date 2026-10-11 so no finer same-day chronological priority is asserted. Independently and earlier (2025-03-06), Denčić et al. Theorem 2.1 and Corollary 2.3 establish the exact normalized q-radius for every rank-one T: omega_r(T)/||T||=(1+r c+sqrt(1-r^2)sqrt(1-c^2))/2. Minimizing the final concave term on c in [0,1] immediately gives the same two endpoints, with all equality cases. The 2026 universal scaled q-spectral theorem supplies the separate coefficient rho_q=max{1,2r/(1+sqrt(1-r^2))}; the submitted 4/5 comparison is solving an elementary scalar equality using already established constants. No exact printed phrase need match: the full mathematical claim is covered by stronger published statements.

## value

FAIL

The constrained norm bound for nonzero rank-one operators is a natural, motivated operator-theoretic observable, and the projection/nilpotent switch is an interpretable parameter boundary. Nevertheless this submission does not determine an independently unknown exact invariant: the complete rank-one operator norm/q-radius comparison with the same equality classes is already a published rho=1 specialization of a two-parameter theorem, and even the older 2025 exact normalized formula reduces the work to a two-endpoint concavity check. The only extra 4/5 observation equates a branch of that known ratio with a known universal coefficient. No new structural lemma, motivated counterexample beyond the already covered extremizers, or uncovered classification remains. This is a useful worked corollary, not a new mathematically valuable result under the stated nontriviality bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
