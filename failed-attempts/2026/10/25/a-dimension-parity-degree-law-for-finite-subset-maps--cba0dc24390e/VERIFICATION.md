---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For closed connected n-manifolds n>=2, the top k-point unordered configuration stratum is connected dimension nk, and the lower-cardinality subset has codimension at least n. Its mod-2 Borel-Moore orientation class gives top H_nk=F2; integral top H_nk=Z exactly for even n oriented (or k=1 and M oriented), otherwise zero for k>=2. A permutation of n-dimensional factors has sign (-1)^n. For smooth f, preimages of a regular unordered configuration of k distinct values are choices of one point in each fiber; the signed or mod2 product yields (deg f)^k, mod2 equal deg2 f. Continuous maps follow by smooth approximation. These are correct arguments. Importantly the top-group classification and natural comparison with SP^k were already published in Kallel-Sjerve Proposition 6.1.

## originality

FAIL

FAIL: Kallel and Sjerve (2009), Proposition 6.1 and Corollary 3.4, already give the all-dimensional top-homology groups of symmetric and finite subset spaces and the natural isomorphism under the canonical quotient. On top degree, the action of SP^k(f) is the product degree (deg f)^k by the standard independent regular-value multiplication. Naturality transports that same action to Sub_k(f). Thus the entire proposed extension, including mod2, is a direct consequence of an explicitly identified stronger published topological statement and standard degree multiplicativity. Tuffley supplied earlier surface and circle computations. The absence of identical all-dimensional wording is not originality.

## value

FAIL

FAIL: Once the 2009 all-dimensional natural top-homology identification is used, the map-degree exponent is an elementary k-fold product count, not a new structural lemma, nontrivial boundary, or gap requiring a new calculation. The already-known manifold orientation parity supplies the only caveat; this package does not establish a further independently useful unknown invariant beyond the immediate standard corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
