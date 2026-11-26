# Independent mathematical audit

## correctness

PASS

For the open NOR map F on sets, symmetry gives S⊆F²(S); applying antitonicity and then this inclusion to F(S) yields F³=F. Thus recurrence equals the image (and Fix(F²)) and every orbit enters it within one update. A fixed state is precisely an independent set dominating every excluded vertex. A recurrent state and its unique partner give the two shores of a maximal independent set of the canonical double cover; independence is cross nonadjacency and maximality is exactly the pair of complementary-neighborhood equations. Under ((i,a),t)↦((i,t⊕a),a) the double of the prism is the double of C_n Cartesian-product K₂: a rail edge flips t⊕a, a rung preserves it. The double of C_n is two C_n for even n and a single C_(2n) for odd n. On the prism, a rung has a top vertex, a bottom vertex, or neither; adjacent equal occupied rails violate independence and an empty rung must have opposite occupied neighbors. Ordered pairs and allowed overlapping triples count labelled words by trace, not up to rotation. The exact matrix coefficients give t⁵(t²−t−1)(t²+t+1), hence the Lucas-plus-cube-root trace. All terms and asymptotics follow; counting unlabelled temporal pairs requires dividing the nonfixed recurrent states by two, not taking a spatial quotient.

## originality

FAIL

The all-size prism maximal-independent-set number M_n is expressly documented in OEIS A007040 (2017). The other count is a direct substitution in an existing general counting identity: ten Brinke, van Houten and Bodlaender (2015), §2 p. 188, state that the number of distinct unions of neighborhoods across a cut equals the number of maximal independent sets in its bipartite cut graph. For synchronous open NOR, the outputs are exactly the complements of the unions of the input vertices' neighborhoods. Apply the prior identity to the two natural shores of the canonical double cover: this gives the image size exactly, and the previously proved universal one-step entry identity identifies it with the recurrent count. The double cover is the familiar double of the cycle times K₂ (the t⊕a relabelling above), so the prior prism formula on its components gives M_n² or M_(2n). Subtracting the fixed count and halving gives the exact primitive two-orbit formula. Thus the entire numerical census is covered by prior results and direct reductions, even without a previously printed NOR orbit table for prisms.

## value

FAIL

The labelled orbit counts are natural, but here they are mechanically obtained from a documented exact sequence, the general neighborhood-union identity and the elementary cover relabelling. The transfer calculation is a second derivation of the known sequence, and the asymptotics are immediate from its Lucas growth. The frozen claim contains no independent census of individual basins, equivalence under spatial symmetries, or other new result that survives the prior coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
