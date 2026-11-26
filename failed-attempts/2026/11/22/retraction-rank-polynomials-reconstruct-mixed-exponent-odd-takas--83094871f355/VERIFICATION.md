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

For g=F−F(0), the quandle law gives g(2y−x)=2g(y)−g(x); setting x=0 and y=0 and using the bijection 2:A→A proves additivity. The idempotence equations for F=e+c are e²=e and e(c)=0. An additive projection corresponds to an ordered internal decomposition A=U⊕W. Relative to the exponent blocks, the action modulo p is block triangular because maps from the elementary summand into the exponent-p² block have image in its p-multiples; the two diagonal blocks must be invertible and suffice by the finite p-group lifting criterion. Counting lifts and off-diagonal entries gives Γ_p, and the block-diagonal stabilizer gives the ratio of Γ_p factors. The p^{|exponent|} factor in the formula counts the elements of W, one affine shift per element. Translation removes c by conjugacy and linear conjugacy classifies the ordered decompositions by image type. Only type (0,1) contributes at size p; the ratio of the general-linear factors gives [T^p] as stated, including zero when b=0. The identity is the only full-rank term. Together these recover b and a from any nontrivial polynomial; T identifies the trivial case, and the support assertions follow from the intervals [2r,2r+b].

## originality

FAIL

A distinct same-day generalized-dihedral result already gives a type-resolved census for the same affine idempotents, in greater generality. Its nontrivial group retractions correspond composition-preservingly to affine idempotents over the odd abelian group. For t=1 its Boolean summands are A_0=ker P and A_1=im P; every term is |Aut(A)| |A|/(|Aut(A_0)| |Aut(A_1)| |A_1|). Giving that term the formal mark T^{|A_1|} is precisely the frozen polynomial, not a reconstruction from an unrefined total. Full order and order p single out the same decomposition types; the existing automorphism factor reduces at p to p^{2N−2}(p^b−1)/(p−1). The recovery via prime-power factorization and strict monotonicity is then routine. This is demonstrable coverage by a stronger statement; no publication order is inferred from the common date.

## value

FAIL

The invariant is natural and the characterization is correct. But the exact coefficient data are mechanically supplied by the existing stronger type-allocated census on the identical affine idempotents. In the frozen exponent-at-most-p² range the proposed surviving distinction, top degree plus a geometric sum for the multiplicity of C_p, amounts to elementary inversion of that existing count. This does not establish a separate nonroutine increment to retain as a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
