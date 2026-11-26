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

In the ordinary alternating CE complex, extending covectors on K by zero on t gives dτ=0 and dη=τ∧(η∘T), where T is multiplication by α; the sign disappears over F₂. The Leibniz rule gives the two-term maps D_r induced additively on the exterior powers. In degree r the dimension is dim ker D_r+dim coker D_(r−1), equal by rank–nullity to the sum of two nullities (including endpoints). Since 1,α,…,α^(d−1) form a basis, T has irreducible separable characteristic polynomial of degree d and eigenvalues α^(2^i). After scalar extension, the exterior derivation has sum, not product, eigenvalues; the r-subsets with sum zero are exactly the weight-r codewords. Frobenius closes the kernel under rotation, and the conjugates are nonzero and distinct, excluding weights one and two. For the converse let R=F₂[X]/(X^d−1) act on K through Frobenius. A normal basis makes K free of rank one as an R-module. For C=(g) choose α as the image of h=(X^d−1)/g; (X^d−1)|ch iff g|c by polynomial cancellation even in repeated-root lengths. Distance ≥3 forces α nonzero of Frobenius orbit length d, since a shorter orbit repeats a conjugate. This includes C=0 using h=1, so all listed profiles occur. The Betti consequences follow by coefficients. The degree-three traces are 0 and 1, so only the first cubic gives the possible weight-three relation; both nonidentity roots in the group of order seven are primitive, and the derived ideal is K, forcing Lie isomorphisms to conjugate the two distinct multiplication polynomials. As a separate even-length check, a root of X^4+X+1 is full-degree and trace zero; a weight-three relation and its one-position shift would yield weight two. Its only nonzero word is 1111 and its Betti polynomial is (1+z)(1+z^4).

## originality

PASS

Credit the two-term cochain calculation, zero-sum exterior spectrum and classical cyclic-module machinery; the supported distinct claim is the identification of the precise attainable ordinary binary Lie Betti profiles with all length-d cyclic-code weight enumerators of distance ≥3 multiplied by 1+z. The strongest same-day catalogue overlap has square-zero adjoint action; the closest inspected subset-sum theorem is over a real/complex generalized-cohomology construction. Neither covers this classification.

## value

PASS

The full-degree condition gives a natural irreducible family; its ordinary cohomology initially asks for exterior differential ranks in every degree. The theorem gives an exact independent invariant and the converse answers a realizability question, including the repeated-root case. In particular it separates primitive scalars with different cohomology, explains universal H² vanishing, and detects normality. These are useful structural consequences of the complete classification, not a new name for one computed Betti number or a finite list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
