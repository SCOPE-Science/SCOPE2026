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

The census, maps, orbits, and cyclic descendants are correct. A clean check embeds the descendant into the direct product by g↦(gB(g),B(g)); its closure follows from the identity, and projecting the second factor gives the kernel–image size rule. Values are constant on the sets Kg (right cosets in standard terminology, though the record calls them left): B(kg)=B(g) for k in the kernel. In the order-two kernel case, applying the identity to (r,s) excludes B(r)=r. In the bijective case theta(u)=B^{-1}(u)u is an endomorphism; every nontrivial endomorphism of S3 fixes a nonidentity element (an implementer of an inner automorphism, any nonidentity element for the identity automorphism, or the image transposition for order-two image), excluding bijectivity of u↦theta(u)u^{-1}. For a splitting map B(hl)=l^{-1}, the graph above is H×L; the involution swaps the coordinates, proving the stated pairing. Independently enumerated all 46,656 arrays of six outputs using lexicographic three-letter permutations and composition p[q[i]], filtering by the identity on all 36 pairs. This gives (6,1):1, (2,3):3, (3,2):3, (1,6):1; inner conjugation gives orbits in that order with sizes 1,3,3,1, involution reverses that ordering, and each proper split has orders 1,2,3,3,6,6. The frozen checker was inspected but not executed.

## originality

FAIL

The census is covered by the earlier classified regular subgroups/skew braces of order pq, specialized at p=3, q=2. This is an equivariant bijection on this group, not just a coincidence of descendant isomorphism types. The stated involution quotient is the immediate coordinate swap on the already classified splitting graphs and the two elementary graphs.

## value

FAIL

The natural operator census would have value if it filled a gap, but here all exact counts and structures follow mechanically from an existing classification under an exact equivalence. The two-class quotient adds only interchange of the two coordinates of known graphs. The short direct proof and enumeration are pedagogical checks, not a new independently needed finite invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
