---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For every connected simple cactus G in the canonical zero-sum Euclidean space H, the weighted spanning-tree factorization gives det_H(M)=n product_C k((k-1)/k)^(k-1). Differentiation gives edge-root quadratic form a_e^T M^-1 a_e=1 at bridge weights 1 and cycle weights (k-1)/k, and sum of weights equals dim(H). The signed-root trace inequality and AM-GM certify the unique globally minimal ellipsoid, even allowing nonzero centers. g(k)=log F(k) is strictly increasing and concave for k>2, yielding the triangle minima and balanced bridge-free maxima (including n=2c+1 and tree cases). Independently recomputed rational triangle-plus-bridge reduced determinant 4/3 and all four leverage contacts; finite checks cannot prove all cacti.

## originality

FAIL

FAILED originality, not correctness. The complete October 18, 2026 published cactus-symmetric-edge John/Löwner theorem states exactly the same Löwner matrix with bridge coefficient 1 and cycle coefficient (k-1)/k, all vertex contacts, and an exact absolute volume formula via the same weighted-tree determinant. Inserting its weights gives the identical volume sqrt(n product F(k)). Maximizing/minimizing that earlier exact product at fixed cycle count by elementary monotonicity and concavity yields the submitted endpoint inequalities/equality cases, without new nonstandard facts. The claimed complete theorem is mathematically covered by an earlier stronger result, even though its title emphasizes parity and John ellipsoids.

## value

PASS

Exact optimal ellipsoids of graphical polytopes, effective-resistance contact structure, and prescribed cycle-length extremizers are well-motivated metric invariants of a natural infinite graph family. As mathematics the formula and sharp equality classification are useful; originality nevertheless fails due to the stronger earlier result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
