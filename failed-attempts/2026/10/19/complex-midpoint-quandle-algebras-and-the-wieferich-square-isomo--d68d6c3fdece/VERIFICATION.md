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

The complex Fourier transform transports the midpoint product to pointwise multiplication followed by the character permutation: E_χ E_ψ=0 for χ≠ψ and E_χ²=E_(χ²). Two vectors with zero cross-product have disjoint supports because the permutation is invertible. An isomorphism therefore sends the n basis vectors to vectors with nonempty pairwise disjoint supports in n coordinates, hence to a monomial basis; the square relations force the monomial permutation to conjugate the two doubling permutations. Conversely any such conjugacy yields an isomorphism. Finite abelian duality identifies these cycle types with the types on the original groups. Fixed points of doubling to the rth power count G[2^r−1]; Möbius inversion recovers the cycles, and LTE says the positive p-adic levels sampled by all r are precisely s_p,s_p+1,…. At s_p=1 successive profile differences with initial value zero recover the primary exponents. A Wieferich primary component of order at most p is forced, while for p²|N the C_(p²) versus C_p² substitution preserves every observed profile and changes primary rank, even after multiplying both by the same group of order N/p². For automorphisms, the centralizing permutations and the 2^ℓ−1 scalar choices per ℓ-cycle give the displayed order, including 60 and 882 for C_5 and C_7. The quandle nonisomorphism follows because products of right translations with their inverses generate the regular translation group. Independently, trial division by 2,…,33 proves 1093 prime; repeated exact modular doubling gives residues 1, 1092, 27, 121 for exponents 364,182,52,28 mod 1093 and residues 1 mod 1093² and 1064432260 mod 1093³ for exponent 364. Thus every nonzero point in the two witnesses has orbit length 364 and there are 3282 such cycles. The uploaded script was inspected, not run; its witness function checks the modular orders but does not itself test primality of 1093. The independent trial division supplies that small check.

## originality

FAIL

The algebra classification and automorphism count are immediate applications of the existing Fourier transport for finite midpoint products and the nonsingular evolution-algebra isomorphism rule. The doubling cycle type is a special case of the known functional-graph description of power maps. The sharp reconstruction boundary is not asserted verbatim in the passages reviewed, but the only remaining step is a direct arithmetic consequence of the graph fixed-point data: LTE samples a whole tail of primary torsion counts, and the missing first level makes C_(p²) indistinguishable from C_p². The familiar Wieferich congruence names exactly that case. This is coverage by implication, not a claimed prior printing of the whole theorem.

## value

FAIL

Determining when a quandle algebra remembers its group is well motivated, and the Wieferich example is a useful illustration. But on the stated midpoint family the algebra invariant and automorphism count specialize established structural rules, and the exact boundary is the first-level loss in the known power-map data by routine LTE and primary-exponent differences. The record does not establish an additional nonmechanical reconstruction invariant or solve a distinct case left open by those results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
