---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The expected future descendant-subtree size n/j is independent of the parent of j, and moving that parent changes exactly the descendants’ depths. Thus Cov(1{P_j=i},T_n)=n(1+H_{i-1}-H_{j-1})/[j(j-1)]. Summing and telescoping gives the stated exact covariance; each new normalized summand eventually is strictly negative, and S_infty=(i-1)/i²-Σ_{j>i}j^{-2}=-1/(2i²)+O(i^{-3})<0. Tail comparison gives i² S_{floor(c i² log i),i}->1/c-1/2; unique sign crossing implies N_i/(i² log i)->2. Algebra is correct for i=n, root and n=2 as well. Finite enumeration is supportive, not proof.

## originality

FAIL

A previously published November 1 recursive-tree result gives exactly the identical labeled covariance under the notations F_(n,j) and L_n, namely n/j−1+Σ_(s=j)^(n−1)(1/s−n/s²). Its first-passage birth-rank crossing j_n~√(n/log n) and proven unique crossing imply the present fixed-label horizon crossover N_i~2i²log i by asymptotic inversion and the current monotone-in-horizon argument. The same current local indicator formula is explicitly printed in another November 8 published record. The new orientation of the parameter and its reciprocal scaling are corollaries of that earlier stronger formula and do not constitute an original independent claim.

## value

FAIL

The exact marked-vertex dependence and scale would be mathematically meaningful, but they were already published for precisely the same random recursive tree, same covariance, and same array of (n,i). Reparameterizing its sharp rank frontier as an observation-horizon frontier supplies no independently needed unknown invariant or structural gap; replication of already resolved classification does not establish new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
