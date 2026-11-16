# Scientific review: the first four-symbol surjection Fourier fourth-moment distinction

## Correctness — PASS
The single finite claim compares the complete absolute Fourier histograms of onto-word indicators on \(C_4^n\) and \(V_4^n\) for exactly \(n\in\{4,5,6\}\). `verify_compare.py` enumerates all words and computes each character coefficient by an exact Gaussian-integer tensor Fourier transform; every histogram entry and both fourth-moment totals are asserted. Exact Parseval checks and the separate radix-four and bitwise-Walsh programs `check_cyclic.py` and `check_klein.py` corroborate the calculations. The difference \(1{,}132{,}462{,}080\) is therefore not a floating-point estimate. It proves no unexamined length.

## Originality — PASS under bounded comparison
The previously known complete Klein-four surjection spectrum determines one side but does not compute its cyclic counterpart. The closest published published-finding corpus source, *Exact first-band Fourier sampling spectra on surjective words*, was read at full RESULT.md length: it computes degree-one sampling Gram matrices over a cyclic palette, not the full Fourier coefficient histogram or the two-group fourth-moment comparison. Classical Stirling occupancy literature counts onto words but does not establish the claimed spectral inequality in the examined material. Actual searches for additive energy, Walsh support, cyclic/Klein, Fourier moments and surjective words found no dominating statement. The unresolved possibility of an unindexed equivalent calculation is a priority risk, not a mathematical contradiction.

## Value — PASS
The two groups are the only abelian groups of order four; they support the *same labelled surjection set* but different additive relations. The exact first length at which those different relations become spectrally detectable is a natural finite boundary: rank, smallest positive multiplier and the entire histograms through five positions agree, whereas the fourth moment and additive energy separate at six. This supplies a group-law-sensitive invariant with a precise first witness, rather than a recomputation of the existing Klein-four table. It does not claim a general all-length formula.

The comparison depends on an exhaustive finite certificate and would benefit from independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
