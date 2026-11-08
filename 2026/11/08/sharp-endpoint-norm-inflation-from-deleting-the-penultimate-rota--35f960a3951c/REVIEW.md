# Self-review

## Correctness — PASS
The full matrix-coefficient Peter–Weyl projections have central kernels with coefficients equal to representation dimensions. The \(SO(3)\)/\(SU(2)\) Haar normalization, odd-character formula and sharp convolution endpoint norm identity are explicit. A differentiated finite cosine sum gives the exact weighted kernel. Subtracting the penultimate spin term produces the bounded-variation multiplier \(|2\cos2\theta-1|\) of one high-frequency cosine; all other terms have \(L^1\) mass at most logarithmic. Periodic averaging and an elementary signed integral give both constants. No finite experiment is substituted for an asymptotic argument. The accompanying script independently checks the formulas for sampled cutoffs, angles, and absolute integrals.

## Originality — PASS (provisional priority assessment)
The 1986 Giulini–Travaglini main theorem gives two-sided growth **orders**, not a missing-block constant or inflation ratio (DOI `10.1016/0022-1236(86)90059-5`, inspected primary text). Zhang's 2020 compact Lie group restriction paper (first-public `arxiv:2005.11451v1`) treats irreducible character and eigenfunction \(L^p\) bounds, not this sharp punctured convolution norm. A relevant published exact low-pass result on \(SU(2)\) includes every highest weight and is not a theorem about the even-weight \(SO(3)\) series with one omitted interior spin. Its proof was inspected. The finite cyclic three-character Fourier result with the same numerical constant is an independent abelian problem and does not cover this operator. The 1988 Giacalone–Ricci paper was inaccessible for direct full-text comparison; a specialist-priority risk remains.

## Mathematical value — PASS
Endpoint Lebesgue constants are sharp stability and amplification factors of spectral partial-sum operators. The theorem gives an exact relative penalty for a natural operation—deleting one penultimate irreducible sector from a rotation-group approximation space—and proves the initially counterintuitive **strict asymptotic increase**. It is a motivated, nontrivial spectral-mask invariant rather than an arbitrary finite numerical slice; a full classification of masks is not necessary for its utility.

## Scientific limits and verification status
This is a sharp leading-order theorem, with \(O(\log L)\) error, for exactly the specified one-hole family and the \(L^1\)/\(L^\infty\) endpoints. Its proof does not claim all-finite-\(L\) monotonicity, other masks, or an independent verification. Read `RESULT.md` for the complete derivation and `VERIFICATION.md` for replay details.

Self-review: passed. Independent audit: not yet performed.
