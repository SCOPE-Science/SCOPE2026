---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

If the split leaf has depth d and cherry indicator I, the increments are 1−I, d+2, and 2(d+1)−2Id for K, S, and Q. The last identity adds the two new leaves and removes the old pair only when I=1. Uniform sampling gives conditional means E[I]=2K/n, E[d]=S/n, E[Id]=Q/n. Writing D=Q−2S/3 leads directly to E[D_{n+1}|T_n]=(1−2/n)D_n+2/3 and hence E[D_n]=2n/9 from D_3=2/3. The mean recursions similarly give E[K_n]=n/3 and E[S_n]=2n(H_n−1) from (K_3,S_3)=(1,5). In the law of total covariance, the conditional covariance is −Q/n+2KS/n², and the covariance of conditional means is (1−2/n)(1+1/n) times the old covariance. Combining terms cancels 2/n² in the coefficient and leaves v_{n+1}=(1−1/n)v_n−2/9. From v_3=0, telescoping gives (n−1)v_n=−[n(n−1)−6]/9. The sign, asymptotic and deterministic n=2 case follow. The sentence that the new cherry is two levels below the old parent is a prose slip: the new parent is at d, one edge below the old parent; the new leaves are two edges below that parent. The proof uses the correct depths.

## originality

FAIL

Demonstrably already covered. The earlier Resultary record 47374ff68d84 states both the exact covariance and the same auxiliary cherry-leaf depth expectation, and even uses the same mixed-moment recurrence. The earlier records 2943b7ea14eb and ede1259760b8 independently cover the covariance, respectively in a random-BST formulation and directly for Yule trees.

## value

FAIL

The covariance and depth moment are worthwhile exact measures of Yule tree shape in isolation. As a new finding this record supplies no useful increment: both are already given together with the same recurrence, and the circulated BST and root-split forms give equivalent coverage of the main statistic. Finite rechecking of these exact identities does not make a distinct result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
