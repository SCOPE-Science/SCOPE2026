# Scientific review: Universal dyadic Abelian-power spectra in paperfolding words

## Correctness — PASS

The precise domain is any infinite \(\pm1\) instruction sequence, any starting integer \(i\ge1\), and any dyadic block length \(2^k\), \(k\ge0\). The claim is not an extrapolation from examples: the even/odd paperfolding recursion proves a repeated halving identity for block sums at all \(k\ge1\); an alternating signed term reduces every equal-block run to a run of balanced blocks; a Boolean two-state encoding forces opposite odd-index indicators within every four positions and hence excludes fourth powers. The density calculations use only two proven facts about valuation residue classes: each sign has conditional density one half within either index parity, and equal adjacent prescribed-sign pairs have conditional density one quarter. These yield the claimed run densities \(1/4\) and \(1/16\), and the separate unit-period constants. Every implicit natural-density existence assertion follows from these finite valuation truncations and conditional-parity identities.

The extracted standalone verifier returns `VERIFY_OK assertions= 3154986` across exhaustive finite instruction choices and additional long-pattern checks. It supports but does not establish the infinite statements. Remaining correctness risk: an independent specialist has not yet re-derived the proof; this review is not independent validation.

## Originality — PASS (qualified)

The source with closest **same-object, same-instruction** scope is Rob Burns, *The appearance function for paper-folding words* (arXiv:2210.14719, 2022). Its factor-appearance characterization does not state dyadic Abelian-power densities. Holub (arXiv:1207.3585, 2012) establishes Abelian powers of arbitrarily large exponent for all instruction sequences and supplies stratified interval-counting methods, but neither a dyadic exponent ceiling nor the starting-position probability laws was located in the sections inspected. Madill–Rampersad (arXiv:1208.2856, 2012) implies that three Parikh classes exist at every dyadic length for the regular word; that known **support cardinality** is credited rather than claimed new, and by itself it does not fix their frequencies or the equal-block correlations, especially for arbitrary instructions. Fici–Postic–Silva (arXiv:1810.12275, 2018) proves antipower rather than power existence.

Equivalent-formulation checks considered Parikh-vector and balanced-window language; broader-coverage checks considered Holub's universal-power theorem and Madill–Rampersad's class-count recurrences. Relevant indexed mathematical-result comparisons showed no stronger covering result; absence from an index is not proof of novelty. Main residual originality risk: an unindexed paper or a stronger lemma hidden inside general paperfolding factor-frequency work may implicitly imply part of this theorem.

## Mathematical value — PASS

Paperfolding words are canonical 2-adic infinite words exhibiting arbitrarily high Abelian powers when period lengths are unrestricted. The proved **sharp restriction to dyadic periods** is therefore a meaningful structural boundary, not the obvious consequence of an Abelian complexity bound. The exact densities characterize which local repetitions occur at every dyadic scale, without assuming any statistical properties of the folding instructions, and the full Parikh probability distribution strengthens known class-count-only information. The square/cube densities are positive, so the maximum possible dyadic exponent three is attained for every choice of instructions and period. No assertion is made for non-dyadic periods.

## Sources, comparisons and limits

- Burns, *The appearance function for paper-folding words*, https://arxiv.org/abs/2210.14719, first submitted 2022-10-22; same infinite instruction-defined objects, different invariant.
- Holub, *Abelian powers in paper-folding words*, https://arxiv.org/abs/1207.3585, first submitted 2012-07-16; existence of all exponents at some periods, not the dyadic classification.
- Madill–Rampersad, *The abelian complexity of the paperfolding word*, https://arxiv.org/abs/1208.2856, first submitted 2012-08-14; three possible classes at dyadic lengths for the regular word, but not occurrence probabilities or correlations.
- Fici–Postic–Silva, *Abelian Anti-Powers in Infinite Words*, https://arxiv.org/abs/1810.12275, first submitted 2018-10-29; the complementary requirement of pairwise *different* Parikh vectors.

The proof gives actual natural densities rather than finite-prefix counts, and no conclusion on non-dyadic periods. The exact integer verifier is reproducible using only Python 3's standard library.

Self-review: passed. Independent audit: not yet performed.
