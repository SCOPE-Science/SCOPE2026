---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For nontrivial finite abelian A of odd order N, every subgroup not in A has intersection C with A and one outside coset of C, so there are N/|C| such subgroups for each C. Their isomorphism type determines C because the derived subgroup is C (squaring on C is surjective), and they cannot coincide in type with inside subgroups of odd order. An outside subgroup has |C|*|Aut(C)| automorphisms by choosing its restriction on the characteristic odd-order subgroup and the image of a reflection, including C=1. Isomorphisms for each ordered domain/range pair are a torsor under the automorphism group of either. These give h_B^2 a_B(1+N^2/b) per type. Every endomorphism maps A to A by element orders. A reflection image leaves the restriction on A arbitrary; the only possibility when the reflection maps inside A is the trivial map. This yields N|End(A)|+1. Independently, the finite abelian duality identity follows by counting kernels of a given quotient type via their annihilators in the dual group, which is isomorphic to A. Thus the inside sum counts |End(A)|. Weighting by 1+N^2/b>=1+N and using |End(A)|>=2 gives strict inequality. For ordinary D_(2n), each d|n gives one cyclic rotation group of order d and n/d outside groups of size 2d. When n is even, the n reflecting subgroups and rotation C_2 must be combined into a single type, and the n/2 groups V_4 contribute 6(n/2)^2; for d>=3 a dihedral automorphism is determined by a primitive rotation and one reflection, giving d*phi(d). These counts and the totient divisor sum give the asserted all-parity formula. For End, a rotation r-image and a reflection s-image give n^2 maps; two rotation images give 1 or 4 by parity. A reflection r-image is permitted only for even n and then its centralizer contributes four possible s-images of order dividing two. The inequalities follow for n>=3 from d=1 and, for even n, d=2, and plugging in the divisors for p and 2^k gives the stated special cases and unbounded ratio. Algebraic spot checks give (PIso,End)=(18,10),(60,36),(144,64) for n=3,4,6 and (1458,730) for Dih(C_3^2). These evaluations are not new exhaustive counts; the supplied check scripts and expected terminal markers were inspected without executing the scripts. The excluded A=1 and n=2 give abelian equality, as expected.

## originality

PASS

The supported contribution is the full weighted subgroup-isomorphism count for the odd-kernel generalized dihedral family, with exact all-parity ordinary formulas and comparison. The general finite abelian identity, classical subgroup and automorphism ingredients, and Cameron's finite-order strict verifications are not credited as new. The later counterexample to Cameron's universal conjecture is material context but does not cover or contradict these formulas. No equivalent family-level counts were established among the strongest inspected sources.

## value

PASS

The comparison arises from a naturally posed group-counting question, now known not to have a universal positive answer. These formulas quantify how a substantial nonabelian family behaves: they convert the entire odd-kernel answer to intrinsic abelian subgroup-type data, resolve even-kernel type collisions in the ordinary case, and give an unbounded ratio on ordinary 2-power rotation groups. This supplies exact family information unavailable from a positive check at a few small orders or from standard automorphism counts alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
