# Self-review

## Correctness — PASS

The claim and domain agree across all files: odd prime \(p\ge5\), every integer width \(1\le m\le p-1\), real signals, unweighted complete-pair Gini. The proof uses the established prime-group convolution majorization theorem (Lev, as explicitly restated in Madiman–Wang–Woo Lemma 6.3), the elementary Schur convexity of pairwise absolute differences, a coarea reduction for positive linear averaging, and a verified overlap-count identity. The balanced-arc profile formula, monotonicity of the cut-size ratios, complementary-window normalization, and endpoint widths have been checked algebraically. An exact-rational checker corroborates the finite cases; it is not the source of the infinite assertion.

## Originality — PASS (qualified)

The strongest relevant antecedent is Lev's prime-cyclic convolution majorization. It establishes that an arc-interval convolution majorizes every equally sized set convolution, and therefore already provides the central extremizer reduction. However, it does not give the explicit sharp Gini **operator norm** as a function of both prime size and window width or establish the balanced-cardinality optimizer for this quotient. Madiman–Wang–Woo apply the rearrangement to entropy, not the same complete-pair seminorm. Gaubert–Qu determine Hopf oscillation / dual total-variation contraction, a different optimization. Published and published-finding corpus searches for aliases and a matching coefficient found no directly covering expression. Earlier two-tap and three-tap cases are subsumed but cannot imply the new all-width formula. Lev's original full text was inaccessible and an unindexed historical equivalent remains a risk.

## Mathematical value — PASS

This determines an exact attained two-parameter operator seminorm for a canonical family of periodic finite-dimensional averaging operators, rather than a single arbitrarily sliced coefficient. The balanced-arc equality geometry, complementary-width duality, and \(p^{-2}\)-scale contraction deficit have direct relevance to selecting window widths and assessing dispersion suppression. The prime limitation is mathematically motivated by the available rearrangement theorem and is explicitly retained; no claim is made for composite sizes.

## Limitations and audit status

Source-level priority is qualified, especially because the original Lev paper was not available in full. The full prime-cyclic rearrangement statement was read in an accessible later source. The statement does not classify every equality signal or establish composite-order results.

Self-review: passed. Independent audit: not yet performed.
