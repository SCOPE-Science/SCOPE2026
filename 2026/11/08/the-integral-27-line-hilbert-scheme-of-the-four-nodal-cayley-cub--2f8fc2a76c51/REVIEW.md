# Self-review

## Correctness — PASS

The projection-from-node argument classifies all geometric lines as six coordinate edges and three diagonal pairings over **every** algebraically closed field, without reliance on characteristics zero or greater than three. Four explicit Grassmannian coefficient equations, together with the surjective integral map to \(\mathbb Z[u,v]/(u^2,v^2)\), give actual length-four closed subschemes at the six edges; all three diagonal Jacobian determinants are units. The rank-four section on the relative dimension-four Grassmannian is regular on each zero-dimensional fiber, whose length is the top Chern degree \(27\); the constructed disjoint closed subschemes fill that degree. Proper-plus-quasi-finite makes the total scheme finite. Flatness of the constructed rank-27 subscheme, finite base change, and Nakayama force equality with the entire Hilbert scheme, proving the claimed integral isomorphism. The standalone pure-Python verifier confirms the local substitutions, determinants and Chern coefficient; exhaustive finite-field counts for three small characteristics are corroboration only.

## Originality — PASS, qualified

Heath-Brown (2002), Section 1, explicitly provides the same nine geometric lines, with three diagonals and six coordinate lines. Derenthal–Hausen–Heim–Keicher–Laface (2014), Section 3 Table 1, gives the \(4A_1\) reduced line count and Cox-ring classification of the minimal resolution. Neither inspected work describes the **entire relative Hilbert scheme over the integer base**, nor its precise six nonreduced length-four and three reduced factors. The classic statement that a smooth cubic has 27 lines or that the zero-dimensional Grassmannian top Chern class is 27 is not novel and is only a proof input. Targeted searches of mathematical records and relevant primary-source full text did not identify the claimed integral factorization or a stronger equivalent. Historical priority remains provisional for unlocated older degenerations literature; lack of a match is not uniqueness proof.

## Mathematical value — PASS

The four-nodal cubic is the maximally nodal cubic surface. Its classical degeneration from 27 reduced lines to nine reduced supports is not explained by reduced line counts alone. Determining the full flat Hilbert scheme, each local Artin ring, and stability across the most delicate characteristics distinguishes truly nonreduced collision multiplicities from mere enumerative conservation. It supplies a natural complete classification for the canonical line scheme of a distinguished singular algebraic surface, not a routine computation of an arbitrary degree or parameter slice.

## Prior literature and limitations

The closest explicit reduced-line reference is Heath-Brown's 2002 Cayley article (arXiv:math/0210333). The closest systematic \(4A_1\) classification is the 2014 Cox-ring paper (arXiv:1409.0799). The integral finite-scheme theorem is not asserted to resolve an open question posed explicitly in either source. More specialized older sources could already contain equivalent multiplicity computations. All computed certificates were generated in the new result's attached program and only self-review has been performed.

Self-review: passed. Independent audit: not yet performed.
