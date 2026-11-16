# Review of the first-carry moment transition

## Correctness — PASS

The claim concerns normalized Haar moments of a finite flat polynomial. Fourier orthogonality converts the moment to an exact weighted zero-sum problem. At moment order strictly below twice the base, signed digit differences cannot carry, giving independent Vandermonde factors. At the first critical order the reachable integer carries are precisely a subset of \(\{-1,0,1\}\), producing an explicit three-by-three binomial transfer matrix. The central initial state lies in the symmetric invariant sector; the characteristic polynomial, recurrence, nonnegative spectral coefficients, and strict inequality follow by exact algebra. The critical root is positive and greater than the one-digit moment. The independent integer-convolution checker passed 281 assertions over seven bases and four depths. No empirical test is used to infer the infinite theorem.

## Originality — PASS relative to inspected material

The motivating Tang–Wu 2026 manuscript, inspected through its complete accessible HTML text, defines and factors the same digit kernel, but its main results concern a singular-measure maximal operator and mismatch bounds rather than Haar even moments, the universal carry threshold, or an exact critical moment recurrence. Diaconis–Fulman's 2008 full HTML text presents the classical unrestricted digit-carry Markov matrix, not the binomially weighted, zero-output-pinned first-carry matrix. The closest indexed research records concern a single three-frequency quartic resonance, the independent coordinate-character eighth-moment problem, binary Cantor Fourier-determinant volume, or a different three-digit additive energy. None of their retrieved claims covers the stated all-base moment transition. An independently indexed digit-restricted carry-computation account supplies a general method to compute higher moments, so derivational overlap is real; it does not state the evaluated two-eigenvalue formula across all bases in the accessible excerpt. Residual risk includes a classical or computationally tabulated exact equivalent not located in indexed results.

## Value — PASS

The problem is motivated by the canonical finite Fourier spectra of even-base Cantor measures and the change from dissociated to arithmetically resonant powers. The result supplies an exact, **uniform-in-depth** boundary between complete even-moment factorization and genuine digit interaction, valid for every integer base. The first nonfactorizing moment has an explicitly evaluable quadratic law and a sharp growth constant, not merely a finite count or an implementation of a generic transfer routine. This determines the depth-asymptotic Lebesgue growth of the canonical middle-fourth eighth moment and provides a general benchmark for lacunary Riesz-product estimates. It does not claim arbitrary-coefficient extremality, Cantor-measure norm bounds, or any consequence for almost-everywhere convergence.

## Literature and limitations

Tang and Wu, arXiv:2607.27796 (first version July 30, 2026); Diaconis and Fulman, arXiv:0806.3583; Jorgensen–Pedersen (1998); Holte (1997). The closest indexed research items and the generic digit-carry computational account are discussed in the structured audit. General carry transfer techniques are prior work, and equivalent old or unindexed evaluated formulas have not been excluded exhaustively. This is a self-review only.

Self-review: passed. Independent audit: not yet performed.
