---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The assigned derivation correctly takes h_m=1/[2(m-1)], D_{m+1}=D_m+I_m, L_{m+1}=L_m+1-J_m, conditional E[I_m]=h_m D_m, E[J_m]=h_m L_m, E[I_m J_m]=h_m 1_{D_m=1}. Hence c_{m+1}-c_m=h_m² a_m b_m-h_m q_m. First moments solve q_m=binom(2m-4,m-2)/4^{m-2}, a_m=(2m-3)q_m, b_m=2(m-1)/3+4q_m/3; algebra and telescoping give the finite boxed sum. Sign is 0 at n=2,3 and >0 n>=4; central-binomial asymptotic gives 2 sqrt n/(3sqrt pi). Root D(D+1) and leaf variance recurrences give Var D/n ->2-4/pi and Var L/n->1/9, yielding corr ~ sqrt(2/(pi-2))/sqrt n. Independent exact parent-history enumeration through n=8 verified the assigned sum equals the earlier published increment formula and actual covariance.

## originality

FAIL

A full earlier October 13 theorem concerns exactly the same one-edge seed, degree-proportional rule, first vertex degree, all-leaf count, conditional increment, finite covariance sum, positivity and leading 2sqrt n/(3sqrt pi). The assigned finite sum is an elementary telescoped rewriting of the earlier formula. A November 8 affine-attachment theorem additionally implies the δ=0 positivity and leading asymptotic; current extra correlation constant is obtained by substituting the already known marginal variances.

## value

FAIL

The local-global preferential-attachment covariance is interesting, but the entire exact mixed covariance and sign/asymptotic appeared in an earlier published theorem for the identical model. Remaining correlation rate is routine normalization of that existing covariance by known variance asymptotics, not a new structural gap or independently valuable classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
