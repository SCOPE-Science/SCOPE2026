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

For h_r(t)=r^{-1} exp(-t/r) on t>0, inner products give C_ij=1/(r_i+r_j) and contrasts G=B C B^T. Independence of exponentials makes C positive; rank B=K iff the selected K edges are a tree. All tree incidence bases generate the same integral sum-zero lattice with unimodular transforms. Cauchy determinant and rational interpolation R(z)=1-product_j((z-r_j)/(z+r_j)) imply det G=2(sum r_j) product_{i<j}(r_j-r_i)^2/product_{i,j}(r_i+r_j). The strict derivative inequalities for W(a,b) ensure each cut has uniquely minimal adjacent crossing edge; logarithmic MST exchange yields the unique normalized Gram-volume optimum. Finite-product expansion at r_j=r exp(L t_j), fixed K, proves coefficient and L^{K(K-1)}; K=1 gives 1. Independent exact-rational small-tree tests n=3,4,5 counted 3,16,125, respectively, with common determinants and strict chain optimality; no claim that finite tests prove all K.

## originality

PASS

Best of knowledge, the new statement is a specific all-tree equality for a causal exponential Cauchy kernel combined with a strict normalized-design theorem and fixed-rank collision law. Cauchy determinants, graph incidence and MST selection are classical ingredients and are not claimed individually.

## value

PASS

Distinct natural D-optimal design question for choosing K channels from all pairwise differences of K+1 physical lowpass scales. The tree-invariant determinant and sharp strict-cut maximizer give exact non-geometric design classification and stability loss at scale collision; not merely the Cauchy determinant as a textbook exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
