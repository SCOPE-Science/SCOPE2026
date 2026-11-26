---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The neighborhood-square vectors U_i are independent by invertibility of A(H). In both products the nonzero blocks of x give independent coordinate functionals with independent images, so rank L_x is exactly the number of nonzero blocks. The maximal linear subspaces in the rank-at-most-one locus are thus the individual twin blocks; an isomorphism must permute them and preserve their dimensions. Comparing the nonzero block supports in the images of U_i shows the permutation is an automorphism of H and preserves the weighted degrees. Comparing the coefficient in a neighboring block gives F(S_j)=lambda_i S_sigma(j) for every edge ij. Each lambda_i is positive since a nonzero real coordinate vector has positive squared norm. On a block F is a similitude with squared factor lambda_i d_i; evaluating it on S_i gives s_i^2=lambda_i d_i. The edge relations propagate lambda along even walks, giving a single class in the connected nonbipartite case and the two sides in the connected bipartite case. This forces regularity or biregularity. Conversely the given positive cube-root scalings satisfy c_P^2/d_P=c_Q and c_Q^2/d_Q=c_P, and the constant-degree scaling by d is immediate. For K_k the quotient is invertible and k>=3 gives a triangle, so degree n-a_i is constant exactly when part sizes are equal. The adjacency rank of the blow-up is k and nullity is n-k.

## originality

FAIL

The distinct Resultary finding e8128244024e states the same criterion on the full class of blow-ups of connected bases of invertible adjacency, including the complete multipartite consequence. Its catalogue date is later, so this is a coverage finding and does not establish earlier priority or derivation. Narrower earlier sources are not mistaken for exact coverage.

## value

PASS

The hypothesis isolates a natural structural class of singular graphs, not a numerical cutoff: twin duplication allows arbitrarily high adjacency nullity even on a fixed quotient. Intrinsically recognizing the twin blocks through multiplication ranks gives a useful mechanism explaining rigidity, and the classification captures complete multipartite and other families without enumerating isomorphisms. This is intrinsic significance; it does not overcome exact catalogue coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
