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

In the fixed-p strongly critical chain, C=A−I is strictly lower triangular. In (A^h)_{is} the degree in h is at most i−s, and the unique maximal-length path from 1 to i gives leading coefficient c_i/(i−1)!, including the constant at i=1. Orthogonal martingale innovations give the covariance sum, with E[M_{k,s}M_{k,t}]=Σ_{r≤min(s,t)}E[X_{k−1,r}]Γ_r(s,t)+Γ_imm(s,t), where Γ denotes within-vector covariance. Nonnegative offspring with zero mean in forbidden coordinates vanish almost surely. E[X_{k−1,r}]=O(k^r) and E[X_{k−1,1}]=b_1(k−1). Terms outside (s,t)=(1,1) are therefore O(n^(i+j+1−max(s,t)))=O(n^(i+j−1)). In the (1,1) term the innovation variance is vb_1(k−1)+σ_1²; the immigration component, lower kernel terms, and polynomial-sum errors all have degree at most i+j−1. The leading integral is B(2,i+j−1)=1/[(i+j−1)(i+j)]; for i=j=1 the exact sum is vb_1 n(n−1)/2+σ_1²n. All diagonal leading coefficients are positive by the scope assumptions, giving the Pearson limit with O(n⁻¹). The normalized matrix is the Gram matrix of scaled monomials with weight 1−x on [0,1], hence strictly positive definite. The shifted Jacobi polynomial P_r^(1,0)(2x−1) has leading coefficient binom(2r+1,r) and squared norm 1/(2r+2) for that weight; the monic norms and normalization by H_rr give the stated factorial product. The i/j aspect-ratio limit is valid for the constants only, not a growing-type limit of populations.

## originality

FAIL

The central universal correlation formula already appears exactly in Foster and Ney, Theorem 4(iii), Eq. (9.5), for the limiting vector of their decomposable immigration model, whose matching single-type-per-class chain includes the assigned setting. Their raw mixed-moment result also covers leading finite-generation moments under stronger moment assumptions. I did not find an explicit statement of the finite-second-moment covariance error rate or the normalized factorial determinant in the compared sources. Neither is a sufficiently distinct result here: the former is a direct degree bound in the known second-order recursion, and the latter is the standard Jacobi norm product for the already known matrix. This comparison does not use weak convergence alone to infer convergence of covariances.

## value

FAIL

The object and motivation are natural, and the quantitative derivation is a useful exposition of the old limiting correlations. After crediting the earlier matrix, the remaining O(n⁻¹) bound records the first lower polynomial degree of the known second-moment calculation; it gives neither the first finite-size correction nor any uniform control in p or across offspring laws. The determinant and aspect-ratio limit are routine algebraic consequences of that same known matrix. The record does not leave a separately worthwhile new quantitative claim to repair to.

The dated certificate retains the supplied scientific assessment, sources and limitations.
