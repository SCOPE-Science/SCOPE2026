# Scientific review

## Correctness

PASS. All 1,546 matchings are generated once by a finite row-and-column recursion. The 33,554,432 Walsh coefficients, exact signed frequencies and the kernel's absolute Walsh sum are integer-computable from the supplied first program. The second program computes the same full signed histogram from all 376,992 five-row multisets using a separate 32-state transfer recurrence and exact multinomial weights. The two histograms agree exactly. The rank and conditioning follow by character diagonalization; averaging arbitrary projections over translations proves the stated global minimum endpoint norm. Integer overflow does not arise: butterfly entries have absolute value at most 1,546 for the first pass, at most 33,554,432 in the second, and the absolute sum is accumulated in 64-bit integers.

## Originality

PASS under bounded comparison. Mitchell (2004) gives ordinary rook polynomials and computational decomposition; Huo et al. (2007) compute monomer–dimer counts. Their full texts address different invariants. Indexed earlier Fourier calculations for full five-by-five permutation matrices and for three-row partial matchings do not imply the all-partial-matching signed spectrum or its range-projection norm. Searches for signed rook Fourier spectra and all-partial-permutation recovery did not identify an equivalent 5×5 calculation. Remaining risks are unindexed tables and unavailable full text behind some database links.

## Value

PASS. The square complete bipartite board is a standard canonical monomer–dimer model; unlike ordinary matching enumeration, the exact Walsh zero set determines which translation-invariant convolution data can be recovered, and the sharp endpoint norm measures the cost of removing the invisible modes. The result gives both the full sign-sensitive spectral fingerprint and an exact optimum over every linear projection. It is not a routine deduction from unsigned rook numbers. There is no asserted all-size formula.

Self-review: passed. Independent audit: not yet performed.
