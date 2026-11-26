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

Fix the root-containing color class. Its trees are exactly the spanning trees of K_(a,b), since a tree has a unique bipartition once the root class is specified. For edge weight x_i y_j let X=Σx_i and Y=Σy_j. Delete y_b in the weighted Laplacian. The Schur complement of Y diag(x_i) is X diag(y′)−(X/Y)y′(y′)^T. The rank-one determinant factor is y_b/Y, giving the full determinant (Πx_i)(Πy_j) X^(b−1)Y^(a−1), also valid when a or b is one (empty determinant convention). Dividing out vertex factors gives the excess-degree polynomial, and normalizing gives the independent multinomial profiles conditional on the actual partition. The fixed-root marginal is identical for each partition of that size, so averaging gives the shifted binomial given size only. The binomial successive-mass ratio (n−a−d)/(d(a−1)) decreases in a on the common nondegenerate support. Shrinking upper supports keep all LR cross-products weakly ordered, with at least one strict comparison for every pair of sizes; the concentrated a=1 law is at the overall top. This is strict LR in the sense of ordered but unequal laws, not strict inequality on every zero/zero comparison. Hence strictly increasing score expectations fall strictly and the independent-copy covariance identity gives a strict negative sign. The rare-events limit uses (n−a−1)/a→(1−θ)/θ. Independent replay `python3 /workspace/review_reproduction.py 1` enumerated connected edge subsets of n−1 edges for n=3..6, recovering the size/degree counts, partition profiles and 146 LR cross-products. The determinant and ordering argument, not the finite replay, establish the theorem.

## originality

FAIL

A distinct indexed Resultary record states the same root conditional law, reverse likelihood-ratio order, and strict covariance result. The remaining two-sided conditional profile is a mechanical normalization of the classical full weighted K_(a,b) tree enumerator; the Poisson limit is the ordinary binomial rare-events limit of the covered law. There is no substantiated distinct contribution left in the frozen claim. This is a finding of mathematical coverage, not a claim of which same-day record was first or an inference from date alone.

## value

FAIL

The local-versus-global dependence question is mathematically natural, but its strongest result here is already represented by an exact matching theorem. Apart from it, normalizing a product of powers and taking the standard binomial limit do not address another gap or leave a useful new invariant to repair and pass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
