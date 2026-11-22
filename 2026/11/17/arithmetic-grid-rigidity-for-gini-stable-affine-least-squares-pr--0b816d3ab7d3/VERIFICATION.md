---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

C PASS: Unweighted affine regression normal equations yield P_t y=bar(y)1 + c(sum c_i y_i)/S. Hence G(P_t y)=(B/S)|sum c_i y_i| with B=sum_{i<j}(t_j-t_i), S=sum c_i². Any real y modulo constants decomposes into a nonnegative sum of upper-level binary cut indicators, and G of that decomposition is the corresponding positive sum k(n-k). This proves the exact dual norm as the maximum over subsets. Rearrangement of strictly increasing c_i makes the largest size-k subset a terminal k-set; its complementary lower set handles signs. Every displayed maximum is attained. Since P_t fixes nonconstant t, L>=1; if L=1, its support inequality is tight at the strictly increasing t where G is differentiable with gradient 2i-n-1, forcing centered design c proportional to index ranks. Thus only arithmetic grids are nonexpansive; conversely exact B=2S/beta and terminal cut coefficient beta/2 yield L=1. For r_i=i-(n+1)/2 and t=r+epsilon h, all terminal normalized cuts are 1/2+epsilon d_k and B/S=2-4epsilon bar(d)+O(epsilon²), giving the claimed positive one-sided cusp for any non-affine h. Independent rational brute-force comparisons of all binary cuts on 78 designs n=2..7 confirm the exact norm and rigidity. The finite enumeration is not the general proof.

## originality

PASS

O PASS (qualified): A published polynomial-Gini theorem already proves the degree-one nonexpansive case on equally spaced sites; it does not classify irregular observation designs, provide their exact induced norm or first-order defect. Published convex-cone regression Gini amplification is a nonlinear projection and does not dominate this linear affine-grid theorem. The earlier Gini-variance support result optimizes a statistic rather than fitting-operator sensitivity. Thus the sharp iff grid rigidity and local directional penalty are additional results. Berztiss 1964 on irregularly spaced polynomial regression is a plausible older source, but its full article remained institutionally inaccessible; this is a concrete priority risk, not a reason to manufacture a FAIL.

## value

PASS

V PASS: Stability of fitted responses under the complete-pair Gini distance is a natural robustness criterion distinct from Euclidean least-squares fit error. The characterization of exactly which designs are nonexpansive, sharp binary worst-case perturbations, explicit 28/25 witness, and nonsmooth linear perturbation penalty solve a motivated full-design parameter classification. This is not a textbook normal-equation identity alone, and neither finite examples nor raw reproducibility were used as a substitute for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
