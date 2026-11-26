---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For either Laplacian projector P₂ or P₄ and each edge vector b=e_i−e_j, bᵀP_j b=1: the squared projection onto the alternating unit vector is 1 and the remaining squared norm is 1. Therefore the Bernoulli covariance correction to T(P_j) relative to (I−phL)P_j(I−phL) is exactly p(1−p)h²∑bbᵀ=p(1−p)h²L. This independently yields the stated K and its symmetric Frobenius representation. Independence across rounds gives E||W_k⋯W_1x||²=xᵀT^k(P)x on the mean-zero space; diagonal coefficients are K^k(1,1)ᵀ. For 0<p<1 and h>0 the positive K (positive diagonal from the no-edge event) has a dominant positive Perron vector, so the rate holds for every nonzero mean-zero vector as well as the worst case. At h=0 it is 1; at p=1 it is the maximum of the two deterministic squared modal multipliers. I independently expanded (tr K)²−4 det K, obtained the stated radical, and found det C=16p³(p+3)>0 with C₁₁>0. The smallest eigenvalue of C gives a strictly positive uniform convexity modulus for λ_max(S) in h. The right slope at zero is −4p. For the upper boundary the derivative divided by p is 7p−3+N/√Q; for p≥3/7 it is positive. Below 3/7 the valid squared sign test factors as −16(p−1)(3p−2)(11p²−8p+1), negative below the smaller root and positive above it. This yields the unique optimizing regime at and around the threshold. At p=1 the unique minimizer is the modal crossover h=1/3, with rate 1/9. As a check on the distinction from the one-step objective, at (p,h)=(3/4,2/5) both row sums equal 7/25 but ∂hR=2/5. Only the common-gain family is optimized, with its feasible range [0,1/2]. The frozen checker was inspected, not executed.

## originality

PASS

A general exact covariance-operator characterization for this failure model is established prior work. The supported additional result is its explicit C₄ mode reduction and the constrained common-gain optimizer switching at a precise reliability. Neither the inspected general characterization nor the related case results supplies that optimization. Priority is assessed only against the evidence inspected.

## value

PASS

The natural gain-design question is whether to use the maximum nonnegative update or back off to improve long-run mean-square convergence. On C₄ the full reliability law gives a precise boundary and an easily tested example where optimizing a one-step surrogate does not optimize long-run decay. The threshold and proof of uniqueness throughout the feasible range are substantive beyond listing eigenvalues for one graph or one parameter point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
