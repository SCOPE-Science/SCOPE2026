# Scientific review

## Correctness
**PASS.** The factor-to-two-aligned-block decomposition is exact for all zero-based starts. Every residue phase pair is realized by a constructive binary integer, and dyadic prefix differences satisfy the displayed minimum/maximum recurrences. The Fourier identity makes their coefficients six-periodic; the base levels and explicit level-2 to level-8 comparison establish the six-step induction for all levels. Every intermediate integer is attained because individual prefix differences change by at most one and the anchored intervals connect. `verify.py` replays the finite tables and independent direct-factor tests. Finite checks are supplementary, not the infinite proof.

## Originality
**PASS, qualified.** The most relevant prior work is Chen–Wen–Wu, arXiv:1802.03610, which proves the additive-complexity and pair-difference extrema for the same length-two ternary morphism; it does not assert the single-symbol frequency spectrum. Popoli–Shallit–Stipulanti, arXiv:2410.02409, restate that additive result without giving this one-coordinate projection. Chen–Wen, arXiv:1809.06554, address a distinct length-equals-alphabet substitution family. Actual title/claim/equivalence and research-index searches found no corresponding claim, although an unindexed equivalent remains possible.

## Value
**PASS.** The theorem is a sharp, all-dyadic-length, three-letter counting invariant of a classical automatic word. It answers which frequencies of a fixed symbol are possible, rather than just their numerical letter-weighted sums. This is directly useful for bounds on the full Parikh spectrum and abelian complexity; the precise integer interval and its exact sharp logarithmic width are not obtained merely by renaming or substituting parameters into the additive result. It makes no claim about the full abelian spectrum.

## Scope and limitations
All three axes refer to the same one-coordinate frequency claim. The whole two-coordinate Parikh set and nondyadic lengths remain unproved. Independent scientific validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
