---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Let a_j=j−(n+1)/2 and S=∑a_j²=n(n²−1)/12. The squared-displacement definition is exactly ρ=(∑a_j a_(Π(j)))/S. Conditional on Π(i)=i, every other position has expected centered score −a_i/(n−1); since the remaining a's sum to −a_i, the conditional mean is n a_i²/((n−1)S). This equals the stated parabola. The mean of ρ is zero and P(Π(i)=i)=1/n, so division by n gives the coordinate covariance; summing gives 1/(n−1). A sample without replacement from the centered rank scores has variance S/n and distinct-coordinate covariance −S/[n(n−1)], giving Var(ρ)=1/(n−1). For i≠j, E[I_i I_j]=1/[n(n−1)], so E[F]=1 and Var(F)=1. These give the correlation, slope 1, and intercept 1. The endpoint and odd-middle values follow by substitution; n=2 is included, with positive variances and perfect correlation. The formula is for an affine linear projection, not for the conditional expectation of F given ρ. Inspected checker.py and CHECKER_OUTPUT.txt without executing them; a separate enumeration by integer centered-score sums reproduced the displayed moments over 5912 permutations in S_2 through S_7. The proof does not depend on enumeration.

## originality

FAIL

The whole claimed second-moment profile is a direct specialization of the previously published exact variance identity for all permutation assignment sums in Chen and Fang, arXiv:1111.3159, Theorem 1.1(1), equation (1.2). Setting the array deterministic and polarizing gives the exact bilinear statistic here. This is verified prior implication, not an inference from unavailable historical literature, and it does not require that the older paper use the words Spearman or fixed point.

## value

FAIL

The local comparison of two intuitive rank-agreement notions is well motivated and could be a useful example. But the positional and aggregate calibration are exactly routine one-cell and identity-matrix substitutions into the published second-moment formula, with no separate scientific result beyond those substitutions. There is no higher mixed moment, new boundary, or joint law to retain as a distinct valuable claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
