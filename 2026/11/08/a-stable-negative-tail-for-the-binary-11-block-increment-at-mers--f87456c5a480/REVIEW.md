# Review of the Mersenne-shift binary \(11\)-block theorem

## Correctness — PASS

The domain is every integer \(k\ge4\) and every negative difference \(-j\) for \(j\ge1\); the sharpness comparison covers \(k=1,2,3\). The proof defines the carry/adjacency states, proves limiting frequency by a geometric carry bound, explicitly computes the tail vector and checks that it is stationary for zero shift bits. The exact identity \((T_1^4-\tfrac z2T_1^3)(T_1-I)g=0\) is verified coefficient by coefficient by the bundled standalone checker; the induction establishes every \(k\ge4\), and Laurent extraction gives the stated negative tail. Exact initial probabilities and integer samples corroborate, but finite sampling is not used as an infinite proof. The common-denominator method avoids numerical roundoff.

## Originality — PASS within inspected evidence

Sobolewski–Spiegelhofer arXiv:2309.00142 Section 2 explicitly poses the strict-majority problem and proves a Gaussian theorem for many separated one-blocks. Its Proposition 3.2 provides general recurrences but does not establish the present stable negative tail or exact one-block family. Sobolewski arXiv:2204.05287 Theorem 1.7 treats parity-progressions at precisely the same Mersenne step; it does not imply a frequency law for additive increments. The 2024 general block-counting preprint arXiv:2412.15851 is a relevant possible broader source, but only its abstract was accessible in this comparison; its reported many-block Gaussian theorem is not the same exact claim. Searches of available mathematical research records and accessible earlier claims did not identify an equivalent or dominating theorem. Residual uncertainty: unindexed exact results or uninspected later full text.

## Mathematical value — PASS

The theorem resolves an infinite natural family of the explicit strict-majority question rather than an isolated parameter; it reveals an unexpected *full geometric negative-tail stabilization* despite changing nonnegative distributions. The eight-state transfer identity gives a structural explanation and a sharp threshold. This is mathematically distinct from a routine single-shift numerical evaluation and useful for understanding limitations of Gaussian approximations in the one-block regime.

## Scope and limitations

This is not a proof of the strict-majority conjecture for every shift or every binary block. The distribution for \(k\ge4\) is not entirely constant; only its negative side is. Originality review is not a proof of priority, and independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
