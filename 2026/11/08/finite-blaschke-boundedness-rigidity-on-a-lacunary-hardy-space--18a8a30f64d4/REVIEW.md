# Mathematical review: finite-Blaschke boundedness on a lacunary Hardy space

## Correctness
**PASS.** The claimed threshold is checked for all nonconstant finite Blaschke products, with exact quantifiers \(q\ge3\), \(\gamma>0\), and exceptional indices \(q^k\), \(k\ge1\). For nonmonomial products, the boundary argument is real analytic and not affine, so higher-order van der Corput estimates give uniform Fourier-coefficient decay; an exterior-circle Cauchy bound suppresses frequencies larger than a constant multiple of the power. The exceptional set has only logarithmically many indices below that cutoff, so its Fourier energy tends to zero. Parseval makes the weighted norm of \(B^{q^k}\) tend to one, and the input normalized monomials then grow with exact leading coefficient one. For monomials the matrix is orthogonal-column, allowing exact ratios: rotations of powers \(q^j\) are contractive of norm one, while all other degrees yield the asserted divergence. The credited Hilbert–Schmidt theorem's hypotheses hold independently: \(q>2\), complementary weights one, and \(\inf_kq^k/(k+1)^\gamma>0\). The finite checker is corroborative only.

## Originality
**PASS, subject to independent priority checks.** Borichev–Fouchet–Zarouf already prove much sharper uniform Fourier-coefficient bounds for powers of finite Blaschke products; those are explicitly credited and are not new here. Cruz-Zamorano–Dellepiane–Seco already prove Hilbert–Schmidt symbol-class equality for this weight geometry; this is contextual prior input. Lefèvre–Li–Queffélec–Rodríguez-Piazza classify weights on which **every** composition symbol is bounded and analyze automorphism families, rather than the complete family of finite inner symbols on this individual sparse weight. Hou–Jiang's polynomial-growth theory assumes successive weight ratios tend to one, which the present lacunary weight violates. No inspected source provides the exact finite-Blaschke semigroup classification coupled to the universal normalized-power growth. There is residual risk of a broader coefficient-space boundedness criterion entailing the classification as an unrecorded corollary.

## Mathematical value
**PASS.** This is a complete, sharp, degree-independent classification of a natural set of symbols—the finite inner functions—on a natural weight family singled out by contemporary Hilbert–Schmidt composition theory. It distinguishes equality of Hilbert–Schmidt symbol sets from maximal failure of boundedness even on finite inner symbols. The explicit arithmetic surviving semigroup and universal divergence coefficient are more informative than a single counterexample; the result identifies which finite disk coverings survive and quantitatively rules out all others. It does not classify infinite inner symbols.

## Closest literature and limitations
- F. J. Cruz-Zamorano, E. Dellepiane, D. Seco, arXiv:2610.40148v1, Theorem 1.3(b) and Section 4.2: contextual Hilbert–Schmidt equivalence is prior, not novel.
- A. Borichev, K. Fouchet, R. Zarouf, arXiv:2401.17520, Theorem 1 and proof: uniform Fourier coefficient decay is prior, not novel.
- P. Lefèvre, D. Li, H. Queffélec, L. Rodríguez-Piazza, arXiv:2312.03482, Theorem 1.2 and Sections 3–4: classification for all symbols and automorphism regularity.
- B. Hou, C. Jiang, arXiv:2302.08233, Definition 1.1 and introduction: regular weight framework excludes the oscillatory weights used here.

Finite numerical diagnostics verify selected cases only. Generality beyond finite Blaschke products is unproved. Broader implicit coverage remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
